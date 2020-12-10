import unittest
import collections


def run(joltages):
    joltages.insert(0, 0)
    joltages.append(max(joltages)+3)
    joltages.sort()
    diff_one = 0
    diff_three = 0
    for i in range(0, len(joltages)-1):
        diff = joltages[i+1] - joltages[i]
        if diff == 3:
            diff_three += 1
        elif diff == 1:
            diff_one += 1
    return diff_one * diff_three


def part1():
    print(run(read_input()))

#     0
#     1
#     4
#     5
#     6 -> 5 | 4
#     7 -> 6 (5|4) | 5 | 4
#    10 -> 7 -> 6 (5|4) | 5 | 4
#    11 -> 7 -> 6 (5|4) | 5 | 4
#    12 -> 11 | 10 ...


def run2(joltages):
    joltages.insert(0, 0)
    joltages.sort()

    all_options = collections.defaultdict(int)
    all_options[0] = 1

    for i in range(1, len(joltages)):
        jolt = joltages[i]
        pv1 = all_options[jolt-1]
        pv2 = all_options[jolt-2]
        pv3 = all_options[jolt-3]
        all_options[jolt] = pv1 + pv2 + pv3

    return all_options[joltages[-1]]


def part2():
    print(run2(read_input()))


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

    def test_run(self):
        joltages = [int(l) for l in test_input.split('\n')]
        self.assertEqual(run(joltages), 35)

        joltages = [int(l) for l in test_input2.split('\n')]
        self.assertEqual(run(joltages), 220)


class TestPart2(unittest.TestCase):

    def test_run2(self):
        joltages = [int(l) for l in test_input.split('\n')]
        self.assertEqual(run2(joltages), 8)

        joltages = [int(l) for l in test_input2.split('\n')]
        self.assertEqual(run2(joltages), 19208)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
