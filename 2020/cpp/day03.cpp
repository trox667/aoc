#include <cassert>
#include <fstream>
#include <iostream>
#include <set>
#include <tuple>
#include <vector>

typedef std::tuple<int, int> Position;
typedef std::tuple<int, int> Size;

void grid_from_input(const std::vector<std::string> &lines,
                     std::set<Position> &positions, Size &size) {
  int x = 0;
  int y = 0;
  for (auto line : lines) {
    x = 0;
    for (auto c : line) {
      if (c == '#')
        positions.insert(Position(x, y));
      x++;
    }
    y++;
  }
  size = {x, y};
}

bool hit(const std::set<Position> &grid, const Position &position) {
  return grid.find(position) != grid.end();
}

void update_position(const int max_x, Position &position, const int step_x,
                     const int step_y) {
  auto [x, y] = position;
  position = {(x + step_x) % max_x, y + step_y};
}

void read_input(std::vector<std::string> &lines) {
  std::ifstream in("../inputs/input03");
  std::string str;
  while (std::getline(in, str)) {
    if (str.find_first_not_of(' ') != std::string::npos) {
      lines.push_back(str);
    }
  }
}

int run(const std::set<Position> &grid, const Size &size, const int step_x,
        const int step_y) {
  auto [columns, rows] = size;
  Position position = {0, 0};
  int hits = 0;
  while (std::get<1>(position) < rows) {
    update_position(columns, position, step_x, step_y);
    auto [x, y] = position;
    if (hit(grid, position))
      hits++;
  }
  return hits;
}

void part1() {
  std::vector<std::string> lines;
  std::set<Position> grid;
  Size size;
  read_input(lines);
  grid_from_input(lines, grid, size);
  std::cout << run(grid, size, 3, 1) << std::endl;
}

void part2() {
  std::vector<std::string> lines;
  std::set<Position> grid;
  Size size;
  read_input(lines);
  grid_from_input(lines, grid, size);
  std::cout << run(grid, size, 1, 1) * run(grid, size, 3, 1) *
                   run(grid, size, 5, 1) * run(grid, size, 7, 1) *
                   run(grid, size, 1, 2)

            << std::endl;
}

void test_grid_from_input() {
  std::vector<std::string> lines{"..##......."};
  std::set<Position> positions;
  Size size;
  grid_from_input(lines, positions, size);
  assert(positions.size() == 2);
  auto [columns, rows] = size;
  assert(columns == 11);
  assert(rows == 1);
}

void test_hit() {
  std::set<Position> positions{{2, 0}, {3, 0}};
  assert(!hit(positions, {1, 0}));
  assert(hit(positions, {2, 0}));
  assert(!hit(positions, {2, 1}));
}

int main(void) {
  test_grid_from_input();
  test_hit();
  part1();
  part2();
  return 0;
}
