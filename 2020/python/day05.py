import unittest


def parse_code(line):
    row = line[:-3]
    column = line[-3:]
    return (int(row, 2), int(column, 2))


def run(code):
    code = code.replace('F', '0')
    code = code.replace('B', '1')
    code = code.replace('L', '0')
    code = code.replace('R', '1')
    row, column = parse_code(code)
    return row * 8 + column


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
