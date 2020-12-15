#include "hopscotch_map.h"
#include <cassert>
#include <iostream>
#include <tuple>
#include <unordered_map>
#include <vector>

typedef std::uint32_t u32;
typedef std::tuple<u32, u32> PP;
std::vector<u32> read_input() { return std::vector<u32>{14, 1, 17, 0, 3, 20}; }

int run(std::vector<u32>& list, u32 n) {
  u32 turn = 1;
  // std::unordered_map<u32, PP> memory;
  tsl::hopscotch_map<u32, PP> memory;

  for (auto l : list) {
    memory[l] = PP(turn, 0);
    turn++;
  }

  auto last = list.back();
  while (turn <= n) {
    if (memory.find(last) != memory.end()) {
      auto [pre, prepre] = memory[last];
      if (prepre != 0)
        last = pre - prepre;
      else
        last = 0;
    } else {
      memory[last] = PP(turn, 0);
    }

    u32 p = 0;
    if (memory.find(last) != memory.end()) {
      auto [pre, prepre] = memory[last];
      p = pre;
    }
    memory[last] = PP(turn, p);
    turn++;
  }

  return last;
}

void part1() { std::cout << run(read_input(), 2020) << std::endl; }

void part2() { std::cout << run(read_input(), 30000000) << std::endl; }

int main(void) {
  part1();
  part2();
  return 0;
}
