//
// Created by trox667 on 11.12.21.
//

#include "day_11.hpp"
#include <array>
#include <set>

namespace day11 {
    constexpr size_t WIDTH = 10;

    using Point = std::pair<int, int>;
    using EnergyMap = std::vector<std::array<int, WIDTH>>;
    using PointList = std::vector<Point>;
    using Flashed = std::set<Point>;

    [[nodiscard]] EnergyMap
    get_energy_level(const std::vector<std::string> &lines) {
        EnergyMap energy_map(lines.size());
        for (auto y = 0; y < lines.size(); ++y) {
            for (auto x = 0; x < WIDTH; ++x) {
                energy_map[y][x] = lines[y][x] - '0';
            }
        }
        return energy_map;
    }

    [[nodiscard]] PointList
    get_neighbors(const int x, const int y, const int height) {
        auto ns = PointList{{x - 1, y + 1},
                            {x - 1, y},
                            {x - 1, y - 1},
                            {x + 1, y + 1},
                            {x + 1, y},
                            {x + 1, y - 1},
                            {x,     y + 1},
                            {x,     y - 1}};
        auto filtered = PointList{};
        std::copy_if(ns.begin(), ns.end(), std::back_inserter(filtered),
                     [height](const auto &point) {
                         return 0 <= std::get<0>(point) &&
                                std::get<0>(point) < WIDTH &&
                                0 <= std::get<1>(point) &&
                                std::get<1>(point) < height;
                     });
        return filtered;
    }

    [[nodiscard]] PointList
    update(const PointList &positions, EnergyMap &energy_map,
           const Flashed &flashed) {
        PointList flashing;
        for (const auto &position: positions) {
            auto x = std::get<0>(position);
            auto y = std::get<1>(position);
            if (flashed.contains(position)) continue;
            energy_map[y][x] += 1;
            if (energy_map[y][x] > 9) {
                flashing.emplace_back(position);
                energy_map[y][x] = 0;
            }
        }
        return flashing;
    }

    [[nodiscard]] bool sum_is_zero(const EnergyMap &energy_map) {
        const auto height = static_cast<int>(energy_map.size());
        for (auto y = 0; y < height; ++y)
            for (auto x = 0; x < WIDTH; ++x)
                if (energy_map[y][x] > 0) return false;
        return true;
    }

    [[nodiscard]] std::pair<long, long>
    run(const int steps, EnergyMap &energy_map) {
        const auto height = static_cast<int>(energy_map.size());
        auto positions = PointList{};
        for (auto y = 0; y < height; ++y)
            for (auto x = 0; x < WIDTH; ++x)
                positions.emplace_back(x, y);

        auto flash_counter = 0;
        for (auto step = 0; step < steps; ++step) {
            if (sum_is_zero(energy_map)) {
                return std::make_pair(0, step);
            }
            auto curr_flashes = update(positions, energy_map, Flashed{});
            auto skip_flashes = Flashed(curr_flashes.begin(),
                                        curr_flashes.end());
            flash_counter += static_cast<int>(curr_flashes.size());
            while (!curr_flashes.empty()) {
                auto p = curr_flashes.back();
                auto x = std::get<0>(p);
                auto y = std::get<1>(p);
                curr_flashes.pop_back();
                auto n_flashes = update(get_neighbors(x, y, height),
                                        energy_map, skip_flashes);
                flash_counter += static_cast<int>(n_flashes.size());
                for (auto item: n_flashes) {
                    skip_flashes.insert(item);
                    curr_flashes.emplace_back(item);
                }
            }
        }
        return std::make_pair(flash_counter, 0);
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        auto energy_map = get_energy_level(lines);
        return std::get<0>(run(100, energy_map));
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        auto energy_map = get_energy_level(lines);
        return std::get<1>(run(1000, energy_map));
    }
}
