#include <algorithm>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <ostream>
#include <string>
#include <vector>

int main() {
  std::fstream file;
  file.open("../inputs/input2", std::ios::in);
  if (file.is_open()) {

    std::map<std::string, std::uint32_t> play1;
    std::map<std::string, std::uint32_t> play2;
    play1 = {{"A X", 4}, {"A Y", 8}, {"A Z", 3}, {"B X", 1}, {"B Y", 5},
             {"B Z", 9}, {"C X", 7}, {"C Y", 2}, {"C Z", 6}};
    play2 = {{"A X", 3}, {"A Y", 4}, {"A Z", 8}, {"B X", 1}, {"B Y", 5},
             {"B Z", 9}, {"C X", 2}, {"C Y", 6}, {"C Z", 7}};

    std::string line;
    std::uint32_t part1 = 0;
    std::uint32_t part2 = 0;
    while (std::getline(file, line)) {
      part1 += play1[line];
      part2 += play2[line];
    }
    std::cout << "Part 1:" << part1 << std::endl;
    std::cout << "Part 2:" << part2 << std::endl;
  }
}