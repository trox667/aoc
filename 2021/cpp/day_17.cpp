//
// Created by trox667 on 17.12.21.
//


#include "day_17.hpp"

#include "utils.hpp"
#include <iostream>
#include <regex>

namespace day17 {
    struct Area {
        long sx, ex, sy, ey;
    };

    struct Hit {
        long x, y, maxy;
    };

    [[nodiscard]] Area get_input(const std::string &line) {
        std::regex rg(R"(x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+))");
        auto matches = std::smatch{};

        if (std::regex_search(line, matches, rg)) {
            return Area{std::stol(matches[1]), std::stol(matches[2]),
                        std::stol(matches[3]), std::stol(matches[4])};
        }
        return Area{};
    }

    [[nodiscard]] bool hit(const long x, const long y, const Area &area) {
        return area.sx <= x && x <= area.ex && area.sy <= y && y <= area.ey;
    }

    [[nodiscard]] std::optional<long> shoot(long vx, long vy, const Area &area) {
        auto x = 0L;
        auto y = 0L;
        auto maxy = 0L;
        while (x <= area.ex && y >= area.ey) {
            x += vx;
            y += vy;
            maxy = std::max(y, maxy);
            if (hit(x, y, area)) return maxy;
            if (vx > 0) vx -= 1;
            vy -= 1;
        }
        return {};
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        auto area = get_input(lines[0]);
        auto maxy = 0L;
        std::vector<Hit> hits{};
        for (auto x = 1; x <= area.ex; ++x) {
            for (auto y = area.sy; y < 1000; y++) {
                auto curr_maxy = shoot(x, y, area);
                if (curr_maxy.has_value()) {
                    maxy = std::max(maxy, curr_maxy.value());
                    hits.emplace_back(Hit{x, y, curr_maxy.value()});
                }
            }
        }
        std::cout << maxy << std::endl;
        std::cout << hits.size() << std::endl;
        return 0L;
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        return 0;
    }
}

