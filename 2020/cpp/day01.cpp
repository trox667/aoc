#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

bool is_2020(const std::vector<uint32_t> &items) {
  if (std::accumulate(items.begin(), items.end(), 0) == 2020)
    return true;
  return false;
}

uint32_t run(std::vector<uint32_t> &items) {
  for (auto i : items)
    for (auto j : items) {
      if (i == j)
        continue;
      if (is_2020(std::vector<uint32_t>{i, j}))
        return i * j;
    }
  return 0;
}

void read_input(std::vector<uint32_t> &items) {
  std::ifstream in("../inputs/input01");
  std::string str;
  while (std::getline(in, str)) {
    if (str.find_first_not_of(' ') != std::string::npos)
      items.push_back(std::stoi(str));
  }
}

void part1() {
  std::vector<uint32_t> items;
  read_input(items);
  std::cout << run(items) << std::endl;
}

uint32_t run2(std::vector<uint32_t> &items) {
  for (auto i : items)
    for (auto j : items)
      for (auto k : items) {
        if (i == j || i == k || j == k)
          continue;
        if (is_2020(std::vector<uint32_t>{i, j, k}))
          return i * j * k;
      }
  return 0;
}

void part2() {
  std::vector<uint32_t> items;
  read_input(items);
  std::cout << run2(items) << std::endl;
}

void test_is_2020() {
  assert(is_2020(std::vector<uint32_t>{1721, 299}));
  assert(is_2020(std::vector<uint32_t>{1900, 120}));
  assert(!is_2020(std::vector<uint32_t>{0, 1900}));
}

int main(void) {
  test_is_2020();
  part1();
  part2();
  return 0;
}
