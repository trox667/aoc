//
// Created by trox667 on 07.12.21.
//

#include <cassert>
#include <numeric>
#include "utils.hpp"
#include "day_7.hpp"

namespace day7 {
    [[nodiscard]] std::vector<int>
    get_positions(const std::vector<std::string> &lines) {
        assert(!lines.empty());
        auto tokens = utils::split(lines[0], ',');
        std::vector<int> positions(tokens.size());
        std::transform(tokens.cbegin(), tokens.cend(), positions.begin(),
                       [](const auto token) { return std::stoi(token); });
        return positions;
    }

    [[nodiscard]] int fuel_one(int distance) { return distance; }

    [[nodiscard]] int fuel_gauss(int distance) {
        return (distance * distance + distance) / 2;
    }

    [[nodiscard]] int run(const std::vector<int> &positions, int calc_fuel(int)) {
        auto max_pos = std::max_element(positions.cbegin(), positions.cend());
        auto min_fuel = std::numeric_limits<int>::max();
        for (auto i = 0; i <= *max_pos; ++i) {
            auto fuel = 0;
            for (const auto &pos: positions) {
                auto d = std::abs(pos - i);
                fuel += calc_fuel(d);
            }
            min_fuel = std::min(fuel, min_fuel);
        }
        return min_fuel;
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        return run(get_positions(lines), &fuel_one);
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        return run(get_positions(lines), &fuel_gauss);
    }
}
