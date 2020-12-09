import unittest
import itertools


def valid(nums, target):
    combinations = itertools.combinations(nums, 2)
    return target in (sum(c) for c in combinations)


def run(nums, preamble=5):
    i = 0
    for i in range(0, len(nums) - preamble):
        end = i + preamble
        n = nums[i:end]
        target = nums[end]
        if not valid(n, target):
            return target
    return 0


def part1():
    print(run(read_input(), 25))


def run2(nums, target):
    for i in range(0, len(nums)):
        for j in range(2, len(nums)):
            s = sum(nums[i:j])
            if s == target:
                return min(nums[i:j]) + max(nums[i:j])
            elif s > target:
                break


def part2():
    print(run2(read_input(), 88311122))


def read_input():
    with open('../inputs/input09') as input:
        return [int(l) for l in input if not l.isspace()]


test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

test_input2 = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


class TestPart1(unittest.TestCase):
    def test_valid(self):
        nums = [num for num in range(1, 26)]
        self.assertTrue(valid(nums, 26))
        self.assertTrue(valid(nums, 49))
        self.assertFalse(valid(nums, 100))
        self.assertFalse(valid(nums, 50))

    def test_run(self):
        nums = [int(l) for l in test_input.split('\n')]
        self.assertEqual(run(nums), 127)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        nums = [int(l) for l in test_input2.split('\n')]
        self.assertEqual(run2(nums, 127), 62)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
