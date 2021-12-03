//
// Created by trox667 on 03.12.21.
//

#include <iostream>
#include <cassert>
#include <cmath>
#include <tuple>
#include "day_3.hpp"

namespace day3 {

    std::vector<std::string> test = {
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010"
    };

    [[nodiscard]] std::vector<int>
    binary_number_from_lines(const std::vector<std::string> &lines) {
        std::vector<int> result(lines.size());
        std::transform(lines.cbegin(), lines.cend(), result.begin(),
                       [](const std::string &line) {
                           return std::stoi(line, nullptr, 2);
                       });
        return result;
    }


    [[nodiscard]] int pow2(size_t power) {
        return static_cast<int>(pow(2, static_cast<double>(power)));
    }

    [[nodiscard]] int create_mask(size_t length) {
        int mask = 0;
        for (auto i = 0; i < length; ++i) {
            mask += pow2(length - 1 - i);
        }
        return mask;
    }

    [[nodiscard]] int part1(const std::vector<std::string> &lines) {
        assert(!lines.empty());
        auto binary_length = lines[0].size();
        auto binary_numbers = binary_number_from_lines(lines);
        auto half = binary_numbers.size() / 2;

        auto ones = std::vector<int>(binary_length);

        for (auto i = binary_length - 1; i > 0; --i) {
            for (auto binary: binary_numbers) {
                if (binary >> i & 1) {
                    ones[binary_length - 1 - i] += 1;
                }
                // early exit because either we have enough ones or zeroes to
                // know that it's more than half of the items
                if (ones[binary_length - 1 - i] > half) {
                    break;
                }
            }
        }
        int gamma = 0;
        for (auto i = 0; i < binary_length; ++i) {
            if (ones[i] > half) {
                gamma += pow2(binary_length - 1 - i);
            }
        }
        auto mask = create_mask(binary_length);
        return gamma * (gamma ^ mask);
    }

    [[nodiscard]] bool is_common_one(int index,
                                     const std::vector<int> &binary_numbers) {
        auto half = static_cast<size_t>(ceil(
                static_cast<double>(binary_numbers.size()) / 2.0));
        auto ones = 0;

        for (auto binary_number: binary_numbers) {
            if (binary_number >> index & 1) {
                ones++;
            }
            if (ones > half || ones == half) {
                return true;
            }
        }

        return false;
    }

    std::vector<int>
    filter(int index, int value, const std::vector<int> &binary_numbers) {
        std::vector<int> result(binary_numbers.size());
        auto it = std::copy_if(binary_numbers.cbegin(), binary_numbers.cend(),
                               result.begin(),
                               [index, value](int binary_number) {
                                   return (binary_number >> index & 1) == value;
                               });
        result.resize(std::distance(result.begin(), it));
        return result;
    }

    [[nodiscard]] int part2(const std::vector<std::string> &lines) {
        auto binary_length = static_cast<int>(lines[0].size());
        auto binary_numbers = binary_number_from_lines(lines);

        auto oxygen_generator_rating = binary_numbers;
        auto co2_scrubber_rating = binary_numbers;

        for (int i = binary_length - 1; i >= 0; --i) {
            if (oxygen_generator_rating.size() > 1) {
                if (is_common_one(i, oxygen_generator_rating)) {
                    oxygen_generator_rating = filter(i, 1,
                                                     oxygen_generator_rating);
                } else {
                    oxygen_generator_rating = filter(i, 0,
                                                     oxygen_generator_rating);
                }
            }

            if (co2_scrubber_rating.size() > 1) {
                if (is_common_one(i, co2_scrubber_rating)) {
                    co2_scrubber_rating = filter(i, 0, co2_scrubber_rating);
                } else {
                    co2_scrubber_rating = filter(i, 1, co2_scrubber_rating);
                }
            }
        }
        assert(oxygen_generator_rating.size() == 1 &&
               co2_scrubber_rating.size() == 1);
        return oxygen_generator_rating[0] * co2_scrubber_rating[0];
    }
}