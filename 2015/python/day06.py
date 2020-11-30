import unittest


def light(grid, position, state):
    if state == 'toggle':
        s = grid.get(position)
        grid[position] = not s
    elif state == 'on':
        grid[position] = True
    elif state == 'off':
        grid[position] = False


def light_grid(grid, position_start, position_end, state):
    (psx, psy) = position_start
    (pex, pey) = position_end
    for x in range(psx, pex + 1):
        for y in range(psy, pey + 1):
            light(grid, (x, y), state)


def lights_enabled(grid):
    count = 0
    for i in grid:
        if grid[i]:
            count = count + 1
    return count


def parse_instruction(instruction):
    tokens = instruction.split(' ')
    if tokens[0] == 'toggle':
        state = 'toggle'
        (sx, sy) = tokens[1].split(',')
        (ex, ey) = tokens[3].split(',')
        return ((int(sx), int(sy)), (int(ex), int(ey)), state)
    elif tokens[0] == 'turn':
        state = tokens[1]
        (sx, sy) = tokens[2].split(',')
        (ex, ey) = tokens[4].split(',')
        return ((int(sx), int(sy)), (int(ex), int(ey)), state)


def part1():
    grid = {}
    for instruction in read_input():
        start, end, state = instruction
        light_grid(grid, start, end, state)

    print(lights_enabled(grid))


def light2(grid, position, state):
    if grid.get(position) == None:
        grid[position] = 0

    if state == 'toggle':
        grid[position] = grid[position] + 2
    elif state == 'on':
        grid[position] = grid[position] + 1
    elif state == 'off':
        grid[position] = max(0, grid[position] - 1)


def light_grid2(grid, position_start, position_end, state):
    (psx, psy) = position_start
    (pex, pey) = position_end
    for x in range(psx, pex + 1):
        for y in range(psy, pey + 1):
            light2(grid, (x, y), state)


def lights_enabled2(grid):
    count = 0
    for i in grid:
        count = count + grid[i]
    return count


def part2():
    grid = {}
    for instruction in read_input():
        start, end, state = instruction
        light_grid2(grid, start, end, state)

    print(lights_enabled2(grid))


def read_input():
    instructions = []
    with open('input06') as input:
        instructions = [parse_instruction(i) for i in input]
    return instructions


class TestPart1(unittest.TestCase):
    def test_light(self):
        grid = dict()
        grid[(0, 0)] = True
        light(grid, (0, 0), 'toggle')
        light(grid, (1, 0), 'on')
        light(grid, (2, 0), 'off')
        self.assertEqual(grid[(0, 0)], False)
        self.assertEqual(grid[(1, 0)], True)
        self.assertEqual(grid[(2, 0)], False)

    def test_light_grid(self):
        grid = dict()
        light_grid(grid, (0, 0), (999, 999), 'on')
        for x in range(0, 1000):
            for y in range(0, 1000):
                self.assertEqual(grid[(x, y)], True)

        light_grid(grid, (0, 0), (999, 0), 'toggle')
        for x in range(0, 1000):
            self.assertEqual(grid[(x, 0)], False)

        light_grid(grid, (499, 499), (500, 500), 'off')
        self.assertEqual(grid[(498, 499)], True)
        self.assertEqual(grid[(501, 499)], True)
        self.assertEqual(grid[(499, 499)], False)
        self.assertEqual(grid[(500, 499)], False)
        self.assertEqual(grid[(499, 500)], False)
        self.assertEqual(grid[(500, 500)], False)
        self.assertEqual(grid[(498, 500)], True)
        self.assertEqual(grid[(501, 500)], True)

    def test_lights_enabled(self):
        grid = dict()
        light_grid(grid, (0, 0), (999, 999), 'on')
        light_grid(grid, (0, 0), (999, 0), 'toggle')
        light_grid(grid, (499, 499), (500, 500), 'off')
        self.assertEqual(lights_enabled(grid), 1000 * 1000 - 1000 - 4)

    def test_parse_instruction(self):
        self.assertEqual(parse_instruction('turn on 0,0 through 999,999'),
                         ((0, 0), (999, 999), 'on'))

        self.assertEqual(parse_instruction('toggle 0,0 through 999,0'),
                         ((0, 0), (999, 0), 'toggle'))

        self.assertEqual(parse_instruction('turn off 499,499 through 500,500'),
                         ((499, 499), (500, 500), 'off'))

    def test_run(self):
        pass


class TestPart2(unittest.TestCase):
    def test_run2(self):
        grid = dict()
        light_grid2(grid, (0, 0), (0, 0), 'on')
        self.assertEqual(grid.get((0, 0)), 1)
        light_grid2(grid, (0, 0), (0, 0), 'off')
        self.assertEqual(grid.get((0, 0)), 0)
        grid = dict()
        light_grid2(grid, (0, 0), (999, 999), 'toggle')
        for x in range(0, 1000):
            for y in range(0, 1000):
                self.assertEqual(grid[(x, y)], 2)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
