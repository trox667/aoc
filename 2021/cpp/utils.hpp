//
// Created by trox667 on 04.12.21.
//

#pragma once

#include <string>
#include <vector>

namespace utils {

    [[nodiscard]] inline auto split(const std::string &line, char delimiter) {
        std::vector <std::string> tokens{};
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
}
