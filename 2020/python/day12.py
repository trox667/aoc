import unittest

dir_map = {
    'E': {
        ('L', 90): 'N',
        ('L', 180): 'W',
        ('L', 270): 'S',
        ('R', 90): 'S',
        ('R', 180): 'W',
        ('R', 270): 'N',
    },
    'N': {
        ('L', 90): 'W',
        ('L', 180): 'S',
        ('L', 270): 'E',
        ('R', 90): 'E',
        ('R', 180): 'S',
        ('R', 270): 'W',
    },
    'W': {
        ('L', 90): 'S',
        ('L', 180): 'E',
        ('L', 270): 'N',
        ('R', 90): 'N',
        ('R', 180): 'E',
        ('R', 270): 'S',
    },
    'S': {
        ('L', 90): 'E',
        ('L', 180): 'N',
        ('L', 270): 'W',
        ('R', 90): 'W',
        ('R', 180): 'N',
        ('R', 270): 'E',
    }
}


def manhattan_distance(start, end):
    return abs(start[0] + end[0]) + abs(start[1]+end[1])


def instruction(line):
    return (line[0:1], int(line[1:]))


def parse(lines):
    return [instruction(line) for line in lines if not line.isspace()]


def is_turn(dir):
    return dir == 'L' or dir == 'R'


def move(curr, instruction):
    (facing, (x, y)) = curr
    (dir, steps) = instruction

    if is_turn(dir):
        ndir = dir_map[facing][instruction]
        return (ndir, (x, y))

    if dir == 'F':
        dir = facing

    if dir == 'N':
        return (facing, (x, y+steps))
    elif dir == 'S':
        return (facing, (x, y-steps))
    elif dir == 'W':
        return (facing, (x-steps, y))
    elif dir == 'E':
        return (facing, (x+steps, y))


def run(lines):
    instructions = parse(lines)
    curr = ('E', (0, 0))
    for instruction in instructions:
        curr = move(curr, instruction)

    return manhattan_distance((0, 0), curr[1])


def part1():
    print(run(read_input()))

# E 10,4 -> R90 -> S 4,-10
# E 10,4 -> L90 -> N -4,10
# E 10,4 -> R180 -> W -10,-4
# E 10,4 -> L180 -> W -10,-4
# E 10,4 -> L270 -> S 4,-10
# E 10,4 -> R270 -> N -4,10

# N 10,4 -> R90 -> E 4,-10
# N 10,4 -> L90 -> W -4,10
# N 10,4 -> R180 -> S -10,-4
# N 10,4 -> L180 -> S -10,-4
# N 10,4 -> L270 -> S 4,-10
# N 10,4 -> R270 -> W -4,10

# R180 = L180 -> negate(x,y)
# R90 = L270 -> negate(x) - swap(x,y)
# L90 = R270 -> negate(y) - swap(x,y)


def swap(x, y):
    return (y, x)


def negate(v):
    return -v


def move2(curr, instruction):
    (facing, (x, y)) = curr
    (dir, steps) = instruction

    if is_turn(dir):
        ndir = dir_map[facing][instruction]
        if steps == 180:
            return (ndir, (negate(x), negate(y)))
        elif dir == 'R' and steps == 90 or dir == 'L' and steps == 270:
            return (ndir, swap(negate(x), y))
        elif dir == 'R' and steps == 270 or dir == 'L' and steps == 90:
            return (ndir, swap(x, negate(y)))

    if dir == 'N':
        return (facing, (x, y+steps))
    elif dir == 'S':
        return (facing, (x, y-steps))
    elif dir == 'W':
        return (facing, (x-steps, y))
    elif dir == 'E':
        return (facing, (x+steps, y))


def run2(lines):
    instructions = parse(lines)
    wp = ('E', (10, 1))
    ship = (0, 0)
    for instruction in instructions:
        (dir, step) = instruction
        if dir != 'F':
            wp = move2(wp, instruction)
        else:
            (sx, sy) = ship
            (_facing, (wx, wy)) = wp
            ship = (sx + wx * step, sy + wy * step)

    return manhattan_distance((0, 0), ship)


def part2():
    print(run2(read_input()))


def read_input():
    with open('../inputs/input12') as input:
        return [line for line in input]


test_input = """F10
N3
F7
R90
F11"""


class TestPart1(unittest.TestCase):
    def test_manhattan(self):
        self.assertEqual(manhattan_distance((0, 0), (17, 8)), 25)

    def test_instruction(self):
        self.assertEqual(instruction('F10'), ('F', 10))
        self.assertEqual(instruction('N3'), ('N', 3))
        self.assertEqual(instruction('F7'), ('F', 7))
        self.assertEqual(instruction('R90'), ('R', 90))
        self.assertEqual(instruction('R999'), ('R', 999))

    def test_move(self):
        start = ('E', (0, 0))
        r1 = move(start, ('F', 10))
        self.assertEqual(r1, ('E', (10, 0)))
        r2 = move(r1, ('N', 3))
        self.assertEqual(r2, ('E', (10, 3)))
        r3 = move(r2, ('F', 7))
        self.assertEqual(r3, ('E', (17, 3)))
        r4 = move(r3, ('R', 90))
        self.assertEqual(r4, ('S', (17, 3)))
        r5 = move(r4, ('F', 11))
        self.assertEqual(r5, ('S', (17, -8)))

    def test_run(self):
        self.assertEqual(run(test_input.split('\n')), 25)


class TestPart2(unittest.TestCase):
    def test_move2(self):
        # E 10,4 -> R90 -> S 4,-10
        # E 10,4 -> L90 -> N -4,10
        # E 10,4 -> R180 -> W -10,-4
        # E 10,4 -> L180 -> W -10,-4
        # E 10,4 -> L270 -> S 4,-10
        # E 10,4 -> R270 -> N -4,10
        self.assertEqual(move2(('E', (10, 4)), ('R', 90)), ('S', (4, -10)))
        self.assertEqual(move2(('E', (10, 4)), ('L', 90)), ('N', (-4, 10)))
        self.assertEqual(move2(('E', (10, 4)), ('R', 180)), ('W', (-10, -4)))
        self.assertEqual(move2(('E', (10, 4)), ('L', 180)), ('W', (-10, -4)))
        self.assertEqual(move2(('E', (10, 4)), ('L', 270)), ('S', (4, -10)))
        self.assertEqual(move2(('E', (10, 4)), ('R', 270)), ('N', (-4, 10)))

    def test_run2(self):
        self.assertEqual(run2(test_input.split('\n')), 286)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
    pass
