#include <algorithm>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <ostream>
#include <string>
#include <vector>

int main() {
  std::fstream file;
  file.open("../inputs/input1", std::ios::in);
  if (file.is_open()) {
    std::string line;
    std::vector<std::uint32_t> sums;
    std::vector<std::uint32_t> group;
    while (std::getline(file, line)) {
      if (line.empty()) {
        auto sum = std::accumulate(group.begin(), group.end(), 0);
        sums.push_back(sum);
        group.clear();
      } else {
        group.push_back(std::stol(line));
      }
    }

    std::sort(sums.begin(), sums.end(), std::greater<std::uint32_t>());
    if (sums.size() >= 3) {
      std::cout << sums[0] << std::endl;
      std::cout << sums[0] + sums[1] + sums[2] << std::endl;
    }
  }
}