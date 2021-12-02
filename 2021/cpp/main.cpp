#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <string_view>
#include <filesystem>

#include "day1.hpp"
#include "day_2.hpp"

std::vector<std::string> read_file(const std::string_view& path) {
    using namespace std;
    ifstream file;
    string tmp;
    vector<string> lines{};
    file.open(path.data());
    if (file.is_open()) {
        while (getline(file, tmp)) {
            lines.push_back(tmp);
        }
        file.close();
    }
    return lines;
}

int main() {
    {
        const auto lines = read_file(
                "/home/trox667/sw/aoc_new/2021/inputs/input01");
        std::cout << "Day 1 - Part 1: " << day1::part1(lines) << std::endl;
        std::cout << "Day 1 - Part 2: "  << day1::part2(lines) << std::endl;
    }
    {
        const auto lines = read_file(
                "/home/trox667/sw/aoc_new/2021/inputs/input02");
        std::cout << "Day 2 - Part 1: "  << day2::part1(lines) << std::endl;
        std::cout << "Day 2 - Part 2: "  << day2::part2(lines) << std::endl;
    }
    return 0;
}
