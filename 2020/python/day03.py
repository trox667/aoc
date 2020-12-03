import unittest


class Grid:
    def __init__(self, columns, rows):
        self.data = set()
        self.rows = rows
        self.columns = columns

    def add(self, entry):
        self.data.add(entry)


def parse(grid: Grid, y, line):
    x = 0
    for c in line:
        if c == '#':
            grid.add((x, y))
        x = x + 1


def step(grid: Grid, position):
    x, y = position
    return (x, y) in grid.data


def update_position(columns, position, step_x=3, step_y=1):
    x, y = position
    return ((x + step_x) % columns, y + step_y)


def run(grid, step_x=3, step_y=1):
    position = (0, 0)
    hits = 0
    while position[1] < grid.rows:
        position = update_position(grid.columns, position, step_x, step_y)
        if step(grid, position):
            hits = hits + 1
    return hits


def part1():
    grid = read_input()
    print(run(grid))


def part2():
    grid = read_input()
    print(
        run(grid, 1, 1) * run(grid) * run(grid, 5, 1) * run(grid, 7, 1) *
        run(grid, 1, 2))


def read_input():
    with open('../inputs/input03') as input:
        inputs = [i.strip() for i in input if not i.isspace()]
        grid = Grid(len(inputs[0]), len(inputs))
        y = 0
        for i in inputs:
            parse(grid, y, i)
            y = y + 1
        return grid


class TestPart1(unittest.TestCase):
    def test_parse(self):
        grid = Grid(11, 1)
        parse(grid, 0, '..##.......')
        self.assertEqual(grid.data, {(2, 0), (3, 0)})

    def test_step(self):
        grid = Grid(11, 3)
        grid.data = {(2, 0), (3, 0), (0, 1), (4, 1), (8, 1), (1, 2), (6, 2),
                     (9, 2)}
        self.assertEqual(step(grid, (6, 2)), True)

    def test_update_position(self):
        self.assertEqual(update_position(11, (10, 0)), (2, 1))
        self.assertEqual(update_position(11, (0, 0)), (3, 1))
        self.assertEqual(update_position(11, (8, 0)), (0, 1))

    def test_run(self):
        grid = Grid(11, 5)
        grid.data = {(2, 0), (3, 0), (0, 1), (4, 1), (8, 1), (1, 2), (6, 2),
                     (9, 2), (2, 3), (4, 3), (8, 3), (10, 3), (1, 4), (5, 4),
                     (6, 4), (9, 4)}
        self.assertEqual(run(grid), 2)


class TestPart2(unittest.TestCase):
    def test_run(self):
        grid = Grid(11, 5)
        grid.data = {(2, 0), (3, 0), (0, 1), (4, 1), (8, 1), (1, 2), (6, 2),
                     (9, 2), (2, 3), (4, 3), (8, 3), (10, 3), (1, 4), (5, 4),
                     (6, 4), (9, 4)}
        self.assertEqual(run(grid, 1, 2), 1)
        self.assertEqual(run(grid, 7, 1), 2)
        pass


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
