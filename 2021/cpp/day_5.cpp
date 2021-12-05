//
// Created by trox667 on 05.12.21.
//

#include "day_5.hpp"
#include <tuple>
#include <cassert>
#include "utils.hpp"
#include <map>
#include <numeric>

namespace day5 {

    using Point = std::tuple<int, int>;

    struct Line {
        Line(Point &p1, Point &p2) : p1{std::move(p1)}, p2{std::move(p2)} {}

        [[nodiscard]] std::vector<Point> range(bool diagonal = false) const {
            auto result = std::vector<Point>{};
            auto ix = std::get<0>(p1) < std::get<0>(p2) ? 1 : -1;
            auto iy = std::get<1>(p1) < std::get<1>(p2) ? 1 : -1;
            auto dx = std::abs(std::get<0>(p1) - std::get<0>(p2));
            auto dy = std::abs(std::get<1>(p1) - std::get<1>(p2));
            auto c = std::max(dx, dy);

            if (dx != 0 && dy != 0 && !diagonal) { return result; }

            auto x = std::get<0>(p1);
            auto y = std::get<1>(p1);

            result.emplace_back(Point{x, y});

            for (auto i = 0; i < c; ++i) {
                if (dx != 0) x += ix;
                if (dy != 0) y += iy;
                result.emplace_back(Point{x, y});
            }

            return result;
        }

        Point p1;
        Point p2;
    };

    [[nodiscard]] std::vector<Line>
    create_lines(const std::vector<std::string> &input_lines) {
        auto lines = std::vector<Line>{};
        for (const auto &input_line: input_lines) {
            auto pos = input_line.find("->");
            if (pos != std::string::npos) {
                auto tmp = input_line;
                tmp.replace(pos, 2, ",");
                auto tokens = utils::split(tmp, ',');
                auto numbers = std::vector<int>(tokens.size());
                std::transform(tokens.begin(), tokens.end(), numbers.begin(),
                               [](const auto &token) {
                                   return std::stoi(token);
                               });
                assert(numbers.size() == 4);
                auto p1 = Point{numbers[0], numbers[1]};
                auto p2 = Point{numbers[2], numbers[3]};
                lines.emplace_back(Line(p1, p2));
            }

        }
        return lines;
    }

    [[nodiscard]] int
    run(const std::vector<std::string> &lines, bool diagonal = false) {
        auto points = std::map<Point, int>{};
        for (const auto &line: create_lines(lines)) {
            for (const auto &point: line.range(diagonal)) {
                points[point] += 1;
            }
        }
        int sum = 0;
        for (const auto &item: points) {
            if (item.second >= 2) sum++;
        }

        return sum;
    }


    [[nodiscard]] int part1(const std::vector<std::string> &lines) {
        return run(lines);
    }

    [[nodiscard]] int part2(const std::vector<std::string> &lines) {
        return run(lines, true);
    }
}