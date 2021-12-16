//
// Created by trox667 on 04.12.21.
//

#pragma once

#include <string>
#include <vector>
#include <cctype>
#include <algorithm>
#include <bitset>
#include <sstream>
#include <map>

namespace utils {
    static auto hex = std::map<char, int>{{'0', 0},
                                          {'1', 1},
                                          {'2', 2},
                                          {'3', 3},
                                          {'4', 4},
                                          {'5', 5},
                                          {'6', 6},
                                          {'7', 7},
                                          {'8', 8},
                                          {'9', 9},
                                          {'A', 10},
                                          {'B', 11},
                                          {'C', 12},
                                          {'D', 13},
                                          {'E', 14},
                                          {'F', 15},
    };

    [[nodiscard]] inline auto split(const std::string &line, char delimiter) {
        std::vector<std::string> tokens{};
        std::string tmp{};
        for (const auto &c: line) {
            if (c == delimiter || c == '\n') {
                if (tmp.empty()) continue;
                tokens.emplace_back(tmp);
                tmp = "";
            } else {
                tmp += c;
            }
        }
        if (!tmp.empty()) tokens.emplace_back(tmp);
        return tokens;
    }

    [[nodiscard]] inline auto trim(const std::string &token) {
        std::string result{};
        for (const auto &c: token) {
            if (c == ' ' || c == '\n' || c == '\t') continue;
            result += c;
        }
        return result;
    }

    [[nodiscard]] inline bool is_lower(const std::string &token) {
        return std::ranges::all_of(begin(token), end(token),
                                   [](const auto &c) {
                                       return std::islower(c);
                                   });
    }

    [[nodiscard]] inline std::string to_binary(const std::string &line) {
        auto ss = std::stringstream{};
        for (const auto &c: line) {
            auto n = std::bitset<4>(hex[c]);
            ss << n.to_string();
        }
        return ss.str();
    }

    [[nodiscard]] inline long int_from_binary_str(const std::string &s) {
        return std::stol(s, nullptr, 2);
    }
}

