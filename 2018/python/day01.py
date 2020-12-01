import unittest
import functools


def run(frequencies):
    return functools.reduce(lambda x, y: x + y, frequencies, 0)


def part1():
    print(run(read_input()))


def run2(frequencies):
    result = {0}
    count = 0
    while True:
        for frequency in frequencies:
            count += frequency
            if count in result:
                return count
            else:
                result.add(count)


def part2():
    print(run2(read_input()))


def read_input():
    with open('../inputs/input01') as input:
        return [int(i) for i in input if not i.isspace()]


class TestPart1(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run([1, 1, 1]), 3)
        self.assertEqual(run([1, 1, -2]), 0)
        self.assertEqual(run([-1, -2, -3]), -6)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        self.assertEqual(run2([1, -1]), 0)
        self.assertEqual(run2([3, 3, 4, -2, -4]), 10)
        self.assertEqual(run2([-6, 3, 8, 5, -6]), 5)
        self.assertEqual(run2([7, 7, -2, -7, -4]), 14)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
    pass
