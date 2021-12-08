//
// Created by trox667 on 08.12.21.
//

#include <tuple>
#include <set>
#include <map>
#include <array>
#include "day_8.hpp"
#include "utils.hpp"

namespace day8 {
    using StringList = std::vector<std::string>;
    using Input = std::vector<std::pair<StringList, StringList>>;

    const static auto UNIQUE_DIGIT_SEGMENT = std::set<size_t>{2, 3, 4, 7};
    const static auto DIGITS = std::map<char, std::vector<size_t>>{
            {'0', {0, 1, 2, 4, 5, 6}},
            {'1', {2, 5}},
            {'2', {0, 2, 3, 4, 6}},
            {'3', {0, 2, 3, 5, 6}},
            {'4', {1, 2, 3, 5}},
            {'5', {0, 1, 3, 5, 6}},
            {'6', {0, 1, 3, 4, 5, 6}},
            {'7', {0, 2, 5}},
            {'8', {0, 1, 2, 3, 4, 5, 6}},
            {'9', {0, 1, 2, 3, 5, 6}},
    };

    [[nodiscard]] Input
    create_input(const std::vector<std::string> &lines) {
        Input result;
        for (const auto &line: lines) {
            const auto tokens = utils::split(line, '|');
            result.emplace_back(std::make_pair(
                    utils::split(tokens[0], ' '),
                    utils::split(tokens[1], ' '))
            );
        }
        return result;
    }

    void update_segments(const size_t idx, const std::string &word,
                         std::array<char, 7> &segments) {
        for (const auto &c: word) {
            if (std::find(segments.begin(), segments.end(), c) ==
                segments.end()) {
                segments[idx] = c;
                return;
            }
        }
    }

    bool cmp_size(std::string &a, std::string &b) {
        return a.size() < b.size();
    }

    int count_char(StringList &segments, const char &c) {
        int count = 0;
        for (const auto &segment: segments) {
            for (const auto &w: segment)
                if (w == c) count++;
        }
        return count;
    }

    [[nodiscard]] std::array<char, 7> determine_digit(const StringList &words) {
        auto segments = std::array<char, 7>();
        auto iwords = words;
        sort(iwords.begin(), iwords.end(), cmp_size);
        StringList rest;

        for (auto &word: iwords) {
            switch (word.size()) {
                case 2:
                    segments[2] = word.at(0);
                    segments[5] = word.at(1);
                    break;
                case 3:
                    update_segments(0, word, segments);
                    break;
                case 4:
                    update_segments(1, word, segments);
                    update_segments(3, word, segments);
                    break;
                case 7:
                    update_segments(4, word, segments);
                    update_segments(6, word, segments);
                    break;
                default:
                    rest.push_back(word);
            }
        }

        auto lf = StringList{};
        auto ls = StringList{};
        for (auto &word: rest) {
            if (word.size() == 5) lf.push_back(word);
            else if (word.size() == 6) ls.push_back(word);
        }

        if (count_char(lf, segments[1]) != 1) {
            auto tmp = segments[1];
            segments[1] = segments[3];
            segments[3] = tmp;
        }
        if (count_char(ls, segments[2]) != 2) {
            auto tmp = segments[2];
            segments[2] = segments[5];
            segments[5] = tmp;
        }
        if (count_char(ls, segments[4]) != 2) {
            auto tmp = segments[4];
            segments[4] = segments[6];
            segments[6] = tmp;
        }

        return segments;
    }


    [[nodiscard]] char
    digit_from_segment(const std::string &word,
                       const std::array<char, 7> &segment) {
        for (const auto &entry: DIGITS) {
            const auto &key = std::get<0>(entry);
            const auto &digit_segments = std::get<1>(entry);
            if (digit_segments.size() != word.size()) continue;

            auto word_cmp = word;
            sort(word_cmp.begin(), word_cmp.end());
            auto digit_cmp = std::string();
            for (auto c: digit_segments) { digit_cmp += (segment[c]); }
            sort(digit_cmp.begin(), digit_cmp.end());
            if (word_cmp == digit_cmp) {
                return key;
            }
        }
        return ' ';
    }

    [[nodiscard]] long part1(const std::vector<std::string> &lines) {
        const auto &input = create_input(lines);
        int sum = 0;
        for (const auto &item: input) {
            const auto &words = std::get<1>(item);
            for (const auto &word: words) {
                if (UNIQUE_DIGIT_SEGMENT.contains(word.size()))
                    sum++;
            }
        }
        return sum;
    }

    [[nodiscard]] long part2(const std::vector<std::string> &lines) {
        const auto &input = create_input(lines);
        int sum = 0;
        for (const auto &item: input) {
            auto tmp = std::string();
            const auto &segments = determine_digit(std::get<0>(item));
            const auto &words = std::get<1>(item);
            for (const auto &word: words) {
                tmp += digit_from_segment(word, segments);
            }
            sum += std::stoi(tmp);
        }
        return sum;
    }
}
