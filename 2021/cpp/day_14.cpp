//
// Created by trox667 on 14.12.21.
//

#include "day_14.hpp"

#include <limits>
#include <vector>
#include <string>
#include <cassert>
#include <map>

namespace day14 {
    using Rules = std::map<std::string, std::vector<std::string>>;
    using PairsCount = std::map<std::string, long>;

    [[nodiscard]] std::string
    get_polymer(const std::vector<std::string> &lines) {
        assert(lines.size() > 1);
        return lines[0];
    }

    [[nodiscard]] Rules get_rules(const std::vector<std::string> &lines) {
        auto rules = Rules{};
        for (auto i = 1; i < lines.size(); ++i) {
            auto key = lines[i].substr(0, 2);
            auto val = lines[i].substr(6, 1);
            rules[key] = std::vector<std::string>{key.at(0) + val,
                                                  val + key.at(1)};
        }
        return rules;
    }

    [[nodiscard]] PairsCount init(const std::string &polymer) {
        PairsCount pairs_count{};
        for (auto i = 2; i <= polymer.size(); ++i) {
            auto pair = polymer.substr(i - 2, 2);
            pairs_count[pair] += 1L;
        }
        return pairs_count;
    }

    [[nodiscard]] PairsCount
    next_step(const PairsCount &pairs_count,
              const Rules &rules) {
        auto new_pairs_count = PairsCount{};
        for (const auto &item: pairs_count) {
            const auto &pair = item.first;
            const auto &count = item.second;
            auto combinations_it = rules.find(pair);
            auto combinations =
                    rules.cend() != combinations_it ? combinations_it->second
                                                    : std::vector<std::string>{};
            for (const auto &combination: combinations) {
                new_pairs_count[combination] += count;
            }
        }
        return new_pairs_count;
    }

    [[nodiscard]] long count(const PairsCount &pairs_count,
                             const char &last_element) {
        std::map<char, long> element_count{};
        for (const auto &item: pairs_count) {
            const auto &pair = item.first;
            const auto &count = item.second;
            element_count[pair.at(0)] += count;
        }
        element_count[last_element] += 1L;

        auto min = std::numeric_limits<long>::max();
        auto max = 0L;
        for (const auto &item: element_count) {
            const auto &count = item.second;
            if (count < min) min = count;
            if (count > max) max = count;
        }
        return max - min;
    }

    [[nodiscard]] long
    run(const std::vector<std::string> &lines, size_t steps) {
        const auto polymer = get_polymer(lines);
        auto rules = get_rules(lines);
        auto pairs_count = init(polymer);
        for (size_t i = 0; i < steps; ++i) {
            pairs_count = next_step(pairs_count, rules);
        }
        return count(pairs_count, polymer.back());
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        return run(lines, 10);
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        return run(lines, 40);
    }
}