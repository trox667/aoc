//
// Created by trox667 on 04.12.21.
//

#include <cassert>
#include <algorithm>
#include <unordered_set>
#include "day_4.hpp"
#include "utils.hpp"

namespace day4 {

    struct Board {
        Board() : last_marked{0}, completed{false} {};

        void add_row(const std::vector<int> &row) {
            grid.emplace_back(row);
        }

        void mark(const int value) {
            for (auto y = 0; y < 5; ++y) {
                for (auto x = 0; x < 5; ++x) {
                    if (grid[y][x] == value) {
                        int idx = y * 5 + x;
                        marker.emplace(idx);
                        last_marked = value;
                    }
                }
            }
        }

        bool is_completed() {
            for (auto i = 0; i < 5; ++i) {
                // TODO: different way to create the indices
                int idxy0 = i * 5 + 0;
                int idxy1 = i * 5 + 1;
                int idxy2 = i * 5 + 2;
                int idxy3 = i * 5 + 3;
                int idxy4 = i * 5 + 4;

                int idxx0 = 0 * 5 + i;
                int idxx1 = 1 * 5 + i;
                int idxx2 = 2 * 5 + i;
                int idxx3 = 3 * 5 + i;
                int idxx4 = 4 * 5 + i;

                if ((marker.contains(idxy0) && marker.contains(idxy1) &&
                     marker.contains(idxy2) && marker.contains(idxy3) &&
                     marker.contains(idxy4)) ||
                    (marker.contains(idxx0) && marker.contains(idxx1) &&
                     marker.contains(idxx2) && marker.contains(idxx3) &&
                     marker.contains(idxx4))) {
                    completed = true;
                    return true;
                }
            }
            return false;
        }

        int sum_unmarked() {
            int sum = 0;
            for (auto y = 0; y < 5; ++y) {
                for (auto x = 0; x < 5; ++x) {
                    int idx = y * 5 + x;
                    if (!marker.contains(idx)) {
                        sum += grid[y][x];
                    }
                }
            }
            return sum;
        }

        int result() {
            return sum_unmarked() * last_marked;
        }

        std::vector<std::vector<int>> grid{};
        std::unordered_set<int> marker{};
        bool completed;
        int last_marked;
    };

    struct Game {
        explicit Game(std::vector<Board> &boards) : boards{boards} {}

        int run(std::vector<int> &numbers, bool early_exit = true) {
            std::vector<int> results{};
            for (const auto &number: numbers) {
                for (auto &board: boards) {
                    if (board.completed) continue;

                    board.mark(number);
                    if (board.is_completed()) {
                        results.emplace_back(board.result());
                        if (early_exit)
                            return results.front();
                    }
                }
            }
            return results.back();
        }

        std::vector<Board> boards;
    };

    [[nodiscard]] auto get_numbers(const std::vector<std::string> &lines) {
        assert(!lines.empty());

        auto tokens = utils::split(lines[0], ',');
        auto result = std::vector<int>(tokens.size());
        std::transform(tokens.begin(), tokens.end(), result.begin(),
                       [](const std::string &line) {
                           return std::stoi(line);
                       });
        return result;
    }

    [[nodiscard]] auto create_board(const std::vector<std::string> &lines) {
        auto boards = std::vector<Board>{};
        auto tmp = Board{};

        for (int i = 1; i < lines.size(); ++i) {
            const auto &line = lines[i];
            const auto tokens = utils::split(line, ' ');
            auto numbers = std::vector<int>(tokens.size());
            std::transform(tokens.begin(), tokens.end(), numbers.begin(),
                           [](const std::string &line) {
                               return std::stoi(line);
                           });
            tmp.add_row(numbers);
            if ((i) % 5 == 0 && i > 1) {
                boards.emplace_back(tmp);
                tmp = Board{};
            }
        }
        return boards;
    }

    [[nodiscard]] int part1(const std::vector<std::string> &lines) {
        auto numbers = get_numbers(lines);
        auto boards = create_board(lines);
        return Game(boards).run(numbers);
    }

    [[nodiscard]] int part2(const std::vector<std::string> &lines) {
        auto numbers = get_numbers(lines);
        auto boards = create_board(lines);
        return Game(boards).run(numbers, false);
    }
}