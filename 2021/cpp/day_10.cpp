//
// Created by trox667 on 10.12.21.
//

#include "day_10.hpp"
#include <map>
#include <numeric>

namespace day10 {
    static char NOERROR = 'E';
    static std::map<char, char> OPEN_CHUNKS{{'(', ')'},
                                            {'[', ']'},
                                            {'{', '}'},
                                            {'<', '>'}};
    static std::map<char, char> CLOSE_CHUNKS{
            {')', '('},
            {']', '['},
            {'}', '{'},
            {'>', '<'}
    };

    [[nodiscard]] int get_points(char c, bool part_one) {
        if (c == ')') return part_one ? 3 : 1;
        else if (c == ']') return part_one ? 57 : 2;
        else if (c == '}') return part_one ? 1197 : 3;
        else if (c == '>') return part_one ? 25137 : 4;
        return 0;
    }

    [[nodiscard]] std::pair<char, std::vector<char>>
    parse(const std::string &line) {
        auto stack = std::vector<char>{};
        bool has_error = false;
        int i = 0;
        for (const auto c: line) {
            if (OPEN_CHUNKS.contains(c)) {
                stack.emplace_back(c);
            } else if (CLOSE_CHUNKS.contains(c)) {
                if (!stack.empty() && CLOSE_CHUNKS[c] == stack.back()) {
                    stack.pop_back();
                } else {
                    has_error = true;
                }
            }
            if (!has_error) ++i;
        }

        std::vector<char> added{};
        std::reverse(stack.begin(), stack.end());
        for (const auto &s: stack) {
            added.emplace_back(OPEN_CHUNKS[s]);
        }
        return std::make_pair(has_error ? line.at(i) : NOERROR, added);
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        std::vector<int> result(lines.size());
        std::transform(lines.cbegin(), lines.cend(), result.begin(),
                       [](const auto &line) {
                           return get_points(std::get<0>(parse(line)), true);
                       });
        return std::accumulate(result.begin(), result.end(), 0);
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        auto result = std::vector<long>{};
        for (const auto &line: lines) {
            const auto r = parse(line);
            const auto error = std::get<0>(r);
            if (error != NOERROR) continue;
            const auto added = std::get<1>(r);
            auto points = 0L;
            for (const auto &a: added) {
                points *= 5;
                points += get_points(a, false);
            }
            if (points > 0) result.emplace_back(points);
        }
        std::sort(result.begin(), result.end());
        return result[std::midpoint(0, static_cast<int>(result.size()))];
    }
}