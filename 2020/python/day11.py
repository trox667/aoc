import unittest
import collections


class Grid:
    def __init__(self):
        self.data = dict()
        self.width = 0
        self.height = 0

    def add(self, position, value):
        self.data[position] = value


def create_grid(width, height):
    grid = Grid()
    grid.width = width
    grid.height = height
    for y in range(0, height):
        for x in range(0, width):
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


def draw(grid):
    for y in range(0, grid.height):
        line = ''
        for x in range(0, grid.width):
            line += grid.data[(x, y)]
        print(line)


def neighbors(grid, position):
    count = 0
    (px, py) = position
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if not (px + x, py + y) in grid.data:
                continue
            if grid.data[(px + x, py + y)] == '#':
                count += 1
    return count


def rules(grid, new_grid, position):
    nc = neighbors(grid, position)
    seat = grid.data[position]
    if seat == 'L' and nc == 0:
        new_grid.add(position, '#')
    elif seat == '#' and nc >= 4:
        new_grid.add(position, 'L')
    else:
        new_grid.add(position, seat)


def turn(grid):
    new_grid = create_grid(grid.width, grid.height)
    for y in range(0, grid.height):
        for x in range(0, grid.width):
            rules(grid, new_grid, (x, y))
    return new_grid


def count_seats(grid):
    return sum(seat == '#' for seat in grid.data.values())


def run(input):
    grid = parse(input)
    while True:
        new_grid = turn(grid)
        if new_grid.data == grid.data:
            return count_seats(new_grid)
        grid = new_grid


def part1():
    print(run(read_input()))


def in_sight(grid, position):
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
            scale += 1
            check_pos = (px + x * scale, py + y * scale)
    return count


def rules2(grid, new_grid, position):
    nc = in_sight(grid, position)
    seat = grid.data[position]
    if seat == 'L' and nc == 0:
        new_grid.add(position, '#')
    elif seat == '#' and nc >= 5:
        new_grid.add(position, 'L')
    else:
        new_grid.add(position, seat)


def turn2(grid):
    new_grid = create_grid(grid.width, grid.height)
    for y in range(0, grid.height):
        for x in range(0, grid.width):
            rules2(grid, new_grid, (x, y))
    return new_grid


def run2(input):
    grid = parse(input)
    while True:
        new_grid = turn2(grid)
        if new_grid.data == grid.data:
            return count_seats(new_grid)
        grid = new_grid


def part2():
    print(run2(read_input()))


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
        self.assertEqual(run2(test_input.split('\n')), 26)


if __name__ == '__main__':
    # part1()
    part2()
    unittest.main()
    pass
