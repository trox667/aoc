import unittest


def parse_code(line):
    row = line[:-3]
    column = line[-3:]
    return (row, column)


def upper_half(value):
    low, up = value
    return (1+low + ((up-low) >> 1), up)
    # return (up - (up >> 1), up)


def lower_half(value):
    low, up = value
    return (low, low + ((up-low) >> 1))


def run(code):
    row, column = parse_code(code)
    curr_row = (0, 127)
    last_row = ''
    for r in row:
        if r == 'F':
            curr_row = lower_half(curr_row)
            last_row = 'F'
        else:
            curr_row = upper_half(curr_row)
            last_row = 'B'

    curr_column = (0, 7)
    last_column = ''
    for c in column:
        if c == 'L':
            curr_column = lower_half(curr_column)
            last_column = 'L'
        else:
            curr_column = upper_half(curr_column)
            last_column = 'R'

    r = 0
    c = 0
    if last_row == 'F':
        r = curr_row[0]
    else:
        r = curr_row[1]
    if last_column == 'L':
        c = curr_column[0]
    else:
        c = curr_column[1]
    return r * 8 + c


def part1():
    print(max([run(line) for line in read_input()]))


def run2(input):
    seat_ids = [run(line) for line in input]
    for seat_id in seat_ids:
        if not seat_id+1 in seat_ids and seat_id+2 in seat_ids:
            return seat_id+1

    return 0


def part2():
    print(run2(read_input()))


def read_input():
    with open('../inputs/input05') as input:
        return [line.strip() for line in input]


class TestPart1(unittest.TestCase):
    def test_parse_code(self):
        self.assertEqual(parse_code("FBFBBFFRLR"), ("FBFBBFF", "RLR"))

    def test_halfs(self):
        self.assertEqual(lower_half((0, 127)), (0, 63))
        self.assertEqual(lower_half((0, 63)), (0, 31))
        self.assertEqual(upper_half((0, 127)), (64, 127))
        self.assertEqual(upper_half((0, 63)), (32, 63))

    def test_run(self):
        self.assertEqual(run('FBFBBFFRLR'), 357)
        self.assertEqual(run('BFFFBBFRRR'), 567)
        self.assertEqual(run('FFFBBBFRRR'), 119)
        self.assertEqual(run('BBFFBBFRLL'), 820)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        pass


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
