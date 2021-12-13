//
// Created by trox667 on 13.12.21.
//

#include <iostream>
#include <set>
#include "day_13.hpp"
#include "utils.hpp"


namespace day13 {

    using Point = std::pair<int, int>;
    using Instruction = std::pair<char, int>;

    void get_coords_instructions(const std::vector<std::string> &lines,
                                 std::vector<Point> &coords,
                                 std::vector<Instruction> &instructions) {
        for (const auto &line: lines) {
            if (line.starts_with("fold")) {
                const auto tokens = utils::split(line, '=');
                if (tokens[0].ends_with('y')) {
                    instructions.emplace_back(
                            std::make_pair('y', std::stoi(tokens[1])));
                } else {
                    instructions.emplace_back(
                            std::make_pair('x', std::stoi(tokens[1])));
                }
            } else if (!line.empty()) {
                const auto tokens = utils::split(line, ',');
                coords.emplace_back(std::stoi(tokens[0]), std::stoi(tokens[1]));
            }
        }
    }

    void print_coords(const std::vector<Point> &coords) {
        auto maxx = 0;
        auto maxy = 0;
        for (const auto &coord: coords) {
            if (std::get<0>(coord) > maxx) maxx = std::get<0>(coord);
            if (std::get<1>(coord) > maxy) maxy = std::get<1>(coord);
        }
        for (auto y = 0; y <= maxy; ++y) {
            for (auto x = 0; x <= maxx; ++x) {
                if (std::find_if(coords.begin(), coords.end(),
                                 [x, y](const auto &coord) {
                                     return std::get<0>(coord) == x &&
                                            std::get<1>(coord) == y;
                                 }) != coords.end()) {
                    std::cout << '#';
                } else {
                    std::cout << '.';
                }
            }
            std::cout << std::endl;
        }
    }

    [[nodiscard]] std::vector<Point>
    fold(const Instruction &instruction, const std::vector<Point> &coords) {
        auto result = std::set<Point>{};
        for (const auto &coord: coords) {
            const auto x = std::get<0>(coord);
            const auto y = std::get<1>(coord);
            const auto value = std::get<1>(instruction);
            if (std::get<0>(instruction) == 'y') {
                auto ty = value - std::abs(y - value);
                result.insert(std::make_pair(x, ty));
            } else {
                auto tx = value - std::abs(x - value);
                result.insert(std::make_pair(tx, y));
            }
        }
        return std::vector<Point>(result.begin(), result.end());
    }


    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        auto coords = std::vector<Point>{};
        auto instructions = std::vector<Instruction>{};
        get_coords_instructions(lines, coords, instructions);

        for (const auto &instruction: instructions) {
            coords = fold(instruction, coords);
            break;
        }

        return coords.size();
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        auto coords = std::vector<Point>{};
        auto instructions = std::vector<Instruction>{};
        get_coords_instructions(lines, coords, instructions);

        for (const auto &instruction: instructions) {
            coords = fold(instruction, coords);
        }
        std::cout << std::endl;
        print_coords(coords);

        return 0;
    }
}