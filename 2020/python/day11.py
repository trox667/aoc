import unittest
import collections


class Grid:
    def __init__(self):
        self.data = dict()
        self.width = 0
        self.height = 0

    def add(self, position, value):
        self.data[position] = value

    def clone_empty(self):
        grid = Grid()
        grid.width = self.width
        grid.height = self.height
        for y in range(0, self.height):
            for x in range(0, self.width):
                grid.add((x, y), '.')
        return grid


def parse(lines):
    grid = Grid()
    grid.height = len(lines)
    grid.width = len(lines[0])
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            grid.add((x, y), lines[y][x])
    return grid


def adjacent_seats(grid, position, infinite=True):
    count = 0
    dirs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1),
            (1, -1)]

    (px, py) = position
    for dir in dirs:
        (x, y) = dir
        scale = 1
        check_pos = (px + x * scale, py + y * scale)
        while check_pos in grid.data:
            if grid.data[check_pos] == '#':
                count += 1
                break
            elif grid.data[check_pos] == 'L':
                break
            if infinite:
                scale += 1
                check_pos = (px + x * scale, py + y * scale)
            else:
                break
    return count


def neighbors(grid, position):
    return adjacent_seats(grid, position, False)


def in_sight(grid, position):
    return adjacent_seats(grid, position, True)


def turn(grid, neighbor_func, max_adjacent_seats):
    new_grid = grid.clone_empty()
    for y in range(0, grid.height):
        for x in range(0, grid.width):
            rules(grid, new_grid, (x, y), neighbor_func, max_adjacent_seats)
    return new_grid


def rules(grid, new_grid, position, neighbor_func, max_adjacent_seats):
    nc = neighbor_func(grid, position)
    seat = grid.data[position]
    if seat == 'L' and nc == 0:
        new_grid.add(position, '#')
    elif seat == '#' and nc >= max_adjacent_seats:
        new_grid.add(position, 'L')
    else:
        new_grid.add(position, seat)


def run(input, neighbor_func=neighbors, max_adjacent_seats=4):
    grid = parse(input)
    while True:
        new_grid = turn(grid, neighbor_func, max_adjacent_seats)
        if new_grid.data == grid.data:
            return sum(seat == '#' for seat in new_grid.data.values())

        grid = new_grid


def part1():
    print(run(read_input()))


def part2():
    print(run(read_input(), in_sight, 5))


def read_input():
    with open('../inputs/input11') as input:
        return [line for line in input if not line.isspace()]


test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


class TestPart1(unittest.TestCase):
    def test_parse(self):
        grid = parse(test_input.split('\n'))
        self.assertEqual(grid.width, 10)
        self.assertEqual(grid.height, 10)

    def test_neighbors(self):
        grid = parse("""###
#.#
###""".split('\n'))
        self.assertEqual(neighbors(grid, (1, 1)), 8)
        grid = parse("""#.#
#.#
.#.""".split('\n'))
        self.assertEqual(neighbors(grid, (1, 1)), 5)

    def test_run(self):
        self.assertEqual(run(test_input.split('\n')), 37)


class TestPart2(unittest.TestCase):
    def test_in_sight(self):
        grid = parse(""".......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
# ........
...#.....""".split('\n'))
        self.assertEqual(in_sight(grid, (3, 4)), 8)

        grid = parse(""".............
.L.L.#.#.#.#.
.............""".split('\n'))
        self.assertEqual(in_sight(grid, (1, 1)), 0)

        grid = parse(""".##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.""".split('\n'))
        self.assertEqual(in_sight(grid, (3, 3)), 0)

    def test_run2(self):
        self.assertEqual(run(test_input.split('\n'), in_sight, 5), 26)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
    pass
