import unittest


def parse(lines):
    return (int(lines[0]), [int(d) for d in filter(lambda x: x != 'x', lines[1].split(','))])


def run(data):
    (time, bus_ids) = data
    diffs = dict()
    for bus_id in bus_ids:
        diffs[bus_id] = bus_id - time % bus_id
    (bus, d) = min(diffs.items(), key=lambda x: x[1])
    return bus * d


def part1():
    print(run(parse(read_input())))
    pass


def parse2(lines):
    count = 0
    entries = list()
    for i in lines[1].split(','):
        if i != 'x':
            entries.append((count, int(i)))
        count += 1
    return entries


def run2(data):
    # (d, max_bus_id) = data[-1]
    (d, max_bus_id) = max(data, key=lambda x: x[1])
    t = 0
    while True:
        all_true = list()
        for (time, bus_id) in data:
            if (t - (d-time)) % bus_id == 0:
                all_true.append(True)
            else:
                all_true.append(False)
        if all(all_true):
            return t - d
        t += max_bus_id


def part2():
    print(run2(parse2(read_input())))


def read_input():
    with open('../inputs/input13') as input:
        return [line for line in input if not line.isspace()]


test_input = """939
7,13,x,x,59,x,31,19"""


class TestPart1(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse(test_input.split('\n')),
                         (939, [7, 13, 59, 31, 19]))

    def test_run(self):
        self.assertEqual(run(parse(test_input.split('\n'))), 295)


class TestPart2(unittest.TestCase):
    def test_parse2(self):
        parse2(test_input.split('\n'))

    def test_run2(self):
        self.assertEqual(run2(parse2(test_input.split('\n'))), 1068781)
        test_input2 = """1
17,x,13,19"""
        self.assertEqual(run2(parse2(test_input2.split('\n'))), 3417)
        test_input2 = """1
67,7,59,61"""
        self.assertEqual(run2(parse2(test_input2.split('\n'))), 754018)
        test_input2 = """1
1789,37,47,1889"""
        self.assertEqual(run2(parse2(test_input2.split('\n'))), 1202161486)


if __name__ == '__main__':
    part1()
    # part2()
    unittest.main()
