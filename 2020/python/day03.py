import unittest


def parse(grid: set, y, line):
    x = 0
    for c in line:
        if c == '#':
            grid.add((x, y))
        x = x + 1


def step(grid: set, position):
    x, y = position
    hit = 0
    if (x, y) in grid:
        hit = hit + 1
    return hit


def update_position(grid_length, position, step_x=3, step_y=1):
    x, y = position
    if x + step_x >= grid_length:
        return (x + step_x - grid_length, y + step_y)
    return (x + step_x, y + step_y)


def run(grid_length, grid_height, grid, step_x=3, step_y=1):
    position = (0, 0)
    hits = 0
    while position[1] < grid_height:
        position = update_position(grid_length, position, step_x, step_y)
        hits = hits + step(grid, position)
    return hits


def part1():
    grid_length, grid_height, grid = read_input()
    print(run(grid_length, grid_height, grid))


def run2():
    pass


def part2():
    grid_length, grid_height, grid = read_input()
    print(run(grid_length, grid_height, grid, 1, 1) *
          run(grid_length, grid_height, grid) *
          run(grid_length, grid_height, grid, 5, 1) *
          run(grid_length, grid_height, grid, 7, 1) *
          run(grid_length, grid_height, grid, 1, 2))


def read_input():
    with open('../inputs/input03') as input:
        grid = set()
        grid_length = 0
        grid_height = 0
        inputs = [i.strip() for i in input if not i.isspace()]
        grid_height = len(inputs)
        grid_length = len(inputs[0])
        y = 0
        for i in inputs:
            parse(grid, y, i)
            y = y+1
        return (grid_length, grid_height, grid)


class TestPart1(unittest.TestCase):
    def test_parse(self):
        grid = set()
        parse(grid, 0, '..##.......')
        self.assertEqual(grid, {(2, 0), (3, 0)})

    def test_step(self):
        grid = {(2, 0), (3, 0), (0, 1), (4, 1), (8, 1), (1, 2), (6, 2), (9, 2)}
        self.assertEqual(step(grid, (6, 2)), 1)

    def test_update_position(self):
        self.assertEqual(update_position(11, (10, 0)), (2, 1))
        self.assertEqual(update_position(11, (0, 0)), (3, 1))
        self.assertEqual(update_position(11, (8, 0)), (0, 1))

    def test_run(self):
        grid = {(2, 0), (3, 0), (0, 1), (4, 1), (8, 1), (1, 2), (6, 2), (9, 2),
                (2, 3), (4, 3), (8, 3), (10, 3), (1, 4), (5, 4), (6, 4), (9, 4)}
        self.assertEqual(run(11, 5, grid), 2)


class TestPart2(unittest.TestCase):
    def test_run(self):
        grid = {(2, 0), (3, 0), (0, 1), (4, 1), (8, 1), (1, 2), (6, 2), (9, 2),
                (2, 3), (4, 3), (8, 3), (10, 3), (1, 4), (5, 4), (6, 4), (9, 4)}
        self.assertEqual(run(11, 5, grid, 1, 2), 1)
        pass


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
