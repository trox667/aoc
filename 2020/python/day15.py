import unittest
import collections


def run(L, n=2020):
    turn = 1
    memory = collections.defaultdict(lambda: (0, 0))

    for l in L:
        memory[l] = (turn, 0)
        turn += 1

    last = L[-1]
    while turn <= n:
        if memory[last][1] != 0:
            (pre, prepre) = memory[last]
            last = pre - prepre
        else:
            last = 0

        (pre, prepre) = memory[last]
        memory[last] = (turn, pre)
        turn += 1

    return last


def part1():
    print(run(read_input()))


def part2():
    print(run(read_input(), 30000000))


def read_input():
    return [14, 1, 17, 0, 3, 20]


class TestPart1(unittest.TestCase):
    def test_run(self):
        self.assertEqual(run([0, 3, 6]), 436)
        self.assertEqual(run([1, 3, 2]), 1)
        self.assertEqual(run([2, 1, 3]), 10)
        self.assertEqual(run([1, 2, 3]), 27)
        self.assertEqual(run([2, 3, 1]), 78)
        self.assertEqual(run([3, 2, 1]), 438)
        self.assertEqual(run([3, 1, 2]), 1836)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        self.assertEqual(run([0, 3, 6], 30000000), 175594)
        self.assertEqual(run([1, 3, 2], 30000000), 2578)
        self.assertEqual(run([2, 1, 3], 30000000), 3544142)
        self.assertEqual(run([1, 2, 3], 30000000), 261214)
        self.assertEqual(run([2, 3, 1], 30000000), 6895259)
        self.assertEqual(run([3, 2, 1], 30000000), 18)
        self.assertEqual(run([3, 1, 2], 30000000), 362)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
