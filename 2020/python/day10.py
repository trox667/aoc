import unittest
import itertools


def next_in_range(joltages, joltage, range=3):
    r = list()
    for j in joltages:
        if j <= joltage+3 or j-1 <= joltage+3 or j-2 <= joltage+3 or j-3 <= joltage+3:
            r.append(j)
    if len(r) == 0:
        return (None, None, None)
    joltages.remove(min(r))
    return (joltages, min(r), min(r)-joltage)


def max_jolt(joltages):
    return max(joltages) + 3


def run(joltages):
    one_diff = 0
    three_diff = 0
    curr = 0
    m = max_jolt(joltages)
    while True:
        joltages, curr, r = next_in_range(joltages, curr)
        if not joltages and not curr and not r:
            return 0
        if r == 1:
            one_diff += 1
        elif r == 3:
            three_diff += 1
        if curr+3 >= m:
            three_diff += 1
            if one_diff == 0:
                return three_diff
            if three_diff == 0:
                return one_diff
            return one_diff * three_diff


def part1():
    print(run(read_input()))


def run2(joltages):
    pass


def part2():
    pass


def read_input():
    with open('../inputs/input10') as input:
        return [int(line) for line in input if not line.isspace()]


test_input = """16
10
15
5
1
11
7
19
6
12
4"""

test_input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


class TestPart1(unittest.TestCase):
    def test_next_in_range(self):
        joltages = [int(l) for l in test_input.split('\n')]
        joltages, d, r = next_in_range(joltages, 0)
        self.assertEqual(d, 1)
        self.assertEqual(r, 1)
        joltages, d, r = next_in_range(joltages, 1)
        self.assertEqual(d, 4)
        self.assertEqual(r, 3)
        joltages, d, r = next_in_range(joltages, 4)
        self.assertEqual(d, 5)
        self.assertEqual(r, 1)
        joltages, d, r = next_in_range(joltages, 5)
        joltages, d, r = next_in_range(joltages, 6)
        joltages, d, r = next_in_range(joltages, 7)
        joltages, d, r = next_in_range(joltages, 10)
        self.assertEqual(d, 11)
        self.assertEqual(r, 1)

    def test_run(self):
        joltages = [int(l) for l in test_input.split('\n')]
        self.assertEqual(run(joltages), 35)

        joltages = [int(l) for l in test_input2.split('\n')]
        self.assertEqual(run(joltages), 220)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        joltages = [int(l) for l in test_input.split('\n')]
        self.assertEqual(run2(joltages), 8)


if __name__ == '__main__':
    # part1()
    unittest.main()
    pass
