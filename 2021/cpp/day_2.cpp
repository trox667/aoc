//
// Created by trox667 on 02.12.21.
//

#include <sstream>
#include <iterator>
#include "day_2.hpp"

namespace day2 {
    enum Direction {
        FORWARD,
        UP,
        DOWN
    };

    struct Command {
        Direction direction;
        std::uint32_t step;
    };

    std::vector<Command>
    commands_from_lines(const std::vector<std::string> &lines) {
        auto result = std::vector<Command>{};
        for (const auto &line: lines) {
            std::istringstream iss(line);
            const auto vec = std::vector<std::string>(
                    std::istream_iterator<std::string>(iss),
                    std::istream_iterator<std::string>());
            Command command{};
            command.step = std::stoi(vec[1]);
            if (vec[0].starts_with("forward")) {
                command.direction = FORWARD;
            } else if (vec[0].starts_with("up")) {
                command.direction = UP;
            } else if (vec[0].starts_with("down")) {
                command.direction = DOWN;
            }
            result.push_back(command);
        }
        return result;
    }

    int part1(const std::vector<std::string> &lines) {
        const auto commands = commands_from_lines(lines);
        std::uint32_t x = 0;
        std::uint32_t y = 0;
        for (const auto command: commands) {
            switch (command.direction) {
                case FORWARD:
                    x += command.step;
                    break;
                case DOWN:
                    y += command.step;
                    break;
                case UP:
                    y -= command.step;
                    break;
                default:
                    break;
            }
        }
        return static_cast<int>(x * y);
    }

    int part2(const std::vector<std::string> &lines) {
        const auto commands = commands_from_lines(lines);
        std::uint32_t x = 0;
        std::uint32_t y = 0;
        std::uint32_t aim = 0;
        for (const auto command: commands) {
            switch (command.direction) {
                case FORWARD:
                    y += command.step * aim;
                    x += command.step;
                    break;
                case DOWN:
                    aim += command.step;
                    break;
                case UP:
                    aim -= command.step;
                    break;
                default:
                    break;
            }
        }
        return static_cast<int>(x * y);
    }
}