import unittest
import collections


def bbox(grid):
    minx = miny = minz = 0
    maxx = maxy = maxz = 0
    for position in grid:
        (px, py, pz) = position
        if px < minx:
            minx = px
        if py < miny:
            miny = py
        if pz < minz:
            minz = pz
        if px > maxx:
            maxx = px
        if py > maxy:
            maxy = py
        if pz > maxz:
            maxz = pz
    return ((minx, miny, minz), (maxx, maxy, maxz))


def bbox2(grid):
    minx = miny = minz = minw = 0
    maxx = maxy = maxz = maxw = 0
    for position in grid:
        (px, py, pz, pw) = position
        if px < minx:
            minx = px
        if py < miny:
            miny = py
        if pz < minz:
            minz = pz
        if pw < minw:
            minw = pw
        if px > maxx:
            maxx = px
        if py > maxy:
            maxy = py
        if pz > maxz:
            maxz = pz
        if pw > maxw:
            maxw = pw
    return ((minx, miny, minz, minw), (maxx, maxy, maxz, maxw))


def draw_grid(grid):
    ((minx, miny, minz), (maxx, maxy, maxz)) = bbox(grid)
    for z in range(minz, maxz + 1, 1):
        print(z)
        for y in range(miny, maxy + 1, 1):
            line = ''
            for x in range(minx, maxx + 1, 1):
                if (x, y, z) in grid:
                    line += '#'
                else:
                    line += '.'
            print(line)
        print()


def create_grid(lines):
    grid = set()
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == '#':
                pos = (x, y, 0)
                grid.add(pos)
    return grid


def adjacent_neighbors(grid, position):
    count = 0
    dirs = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                dirs.append((x, y, z))
    dirs.remove((0, 0, 0))
    (px, py, pz) = position
    for (x, y, z) in dirs:
        check_pos = (px + x, py + y, pz + z)
        if check_pos in grid:
            count += 1
    return count


def rules(grid: set, position):
    nc = adjacent_neighbors(grid, position)
    if position in grid and 2 <= nc <= 3:
        return True
    elif not position in grid and nc == 3:
        return True
    return False


def turn(grid):
    new_grid = set()
    frame = bbox(grid)
    ((minx, miny, minz), (maxx, maxy, maxz)) = frame
    for z in range(minz - 2, maxz + 2, 1):
        for y in range(miny - 2, maxy + 2, 1):
            for x in range(minx - 2, maxx + 2, 1):
                position = (x, y, z)
                if rules(grid, position):
                    new_grid.add(position)
    return new_grid


def run(lines):
    grid = create_grid(lines)
    for i in range(0, 6):
        grid = turn(grid)
    return len(grid)


def part1():
    print(run(read_input()))


def create_grid2(lines):
    grid = set()
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == '#':
                pos = (x, y, 0, 0)
                grid.add(pos)
    return grid


def adjacent_neighbors2(grid, position):
    count = 0
    dirs = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                for w in [-1, 0, 1]:
                    dirs.append((x, y, z, w))
    dirs.remove((0, 0, 0, 0))
    (px, py, pz, pw) = position
    for (x, y, z, w) in dirs:
        check_pos = (px + x, py + y, pz + z, pw + w)
        if check_pos in grid:
            count += 1
    return count


def rules2(grid: set, position):
    nc = adjacent_neighbors2(grid, position)
    if position in grid and 2 <= nc <= 3:
        return True
    elif not position in grid and nc == 3:
        return True
    return False


def turn2(grid):
    new_grid = set()
    frame = bbox2(grid)
    ((minx, miny, minz, minw), (maxx, maxy, maxz, maxw)) = frame
    for w in range(minw - 2, maxw + 2, 1):
        for z in range(minz - 2, maxz + 2, 1):
            for y in range(miny - 2, maxy + 2, 1):
                for x in range(minx - 2, maxx + 2, 1):
                    position = (x, y, z, w)
                    if rules2(grid, position):
                        new_grid.add(position)
    return new_grid


def run2(lines):
    grid = create_grid2(lines)
    for i in range(0, 6):
        grid = turn2(grid)
    return len(grid)


def part2():
    print(run2(read_input()))


def read_input():
    with open('../inputs/input17') as input:
        return [line for line in input if not line.isspace()]


test_input = """.#.
..#
###"""


class TestPart1(unittest.TestCase):
    def test_adjacent_neighbors(self):
        grid = create_grid(test_input.split('\n'))
        self.assertEqual(adjacent_neighbors(grid, (1, 1, 0)), 5)

    def test_run(self):
        self.assertEqual(run(test_input.split('\n')), 112)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        pass


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
