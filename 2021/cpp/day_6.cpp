//
// Created by trox667 on 06.12.21.
//

#include "day_6.hpp"
#include "utils.hpp"
#include <array>
#include <numeric>

namespace day6 {
    [[nodiscard]] std::vector<int> create_state(const std::string &input) {
        auto tokens = utils::split(input, ',');
        auto numbers = std::vector<int>(tokens.size());
        std::transform(tokens.cbegin(), tokens.cend(), numbers.begin(),
                       [](const auto &item) { return std::stoi(item); });
        return numbers;
    }

    [[nodiscard]] long run(std::vector<int> &&state, int days = 80) {
        std::array<long, 9> numbers{};
        for (const auto &s: state) numbers[s] += 1; // init
        for (auto i = 0; i < days; ++i) {
            auto new_count = numbers[0]; // how many new fish are created
            numbers[0] = 0; // already marked as new fish
            for (auto j = 1; j < 9; ++j) { // decrement all values
                if (numbers[j] > 0) {
                    numbers[j - 1] = numbers[j];
                    numbers[j] = 0;
                }
            }
            numbers[6] += new_count; // reset
            numbers[8] += new_count; // add new fish
        }
        return std::accumulate(numbers.cbegin(), numbers.cend(), 0L);
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        return run(std::move(create_state(lines[0])));
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        return run(std::move(create_state(lines[0])), 256);
    }
}
