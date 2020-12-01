import unittest
import itertools
import functools


def is_2020(combinations):
    if 0 in combinations:
        False

    if functools.reduce(lambda x, y: x+y, combinations) == 2020:
        return True
    else:
        return False


def run(items, size=2, compare_func=is_2020):
    for combination in itertools.combinations(items, size):
        if compare_func(combination):
            return functools.reduce(lambda x, y: x*y, combination)
    return 0


def part1():
    print(run(read_input()))


def part2():
    print(run(read_input(), 3))


def read_input():
    with open('../inputs/input01') as input:
        return [int(item.strip()) for item in input if not item.isspace()]
    return []


class TestPart1(unittest.TestCase):
    def test_is_2020(self):
        self.assertEqual(is_2020((1721, 299)), True)
        self.assertEqual(is_2020((0, 0)), False)
        self.assertEqual(is_2020((-100, -1900)), False)
        self.assertEqual(is_2020((100, 1900)), False)

    def test_run(self):
        self.assertEqual(run([1721, 299]), 514579)
        self.assertEqual(run([0, 1, 1721, 2, 299]), 514579)


class TestPart2(unittest.TestCase):
    def test_is_2020_3(self):
        self.assertEqual(is_2020((979, 366, 675)), True)
        self.assertEqual(is_2020((0, 1721, 299)), True)

    def test_run2(self):
        self.assertEqual(run([979, 366, 675], 3), 241861950)
        self.assertEqual(run([0, 1, 979, 366, 675, -1, 3], 3), 241861950)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
