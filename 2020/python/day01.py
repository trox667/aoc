import unittest


def is_2020(a, b):
    if min(a, b) == 0:
        False
    if a + b == 2020:
        return True
    else:
        return False


def run(items):
    for i in range(0, len(items)):
        for j in range(0, len(items)):
            if i == j:
                continue
            a = items[i]
            b = items[j]
            if is_2020(a, b):
                return a * b


def part1():
    with open('../inputs/input01') as input:
        print(run([int(item.strip()) for item in input if not item.isspace()]))


def is_2020_3(a, b, c):
    if min(a, b, c) == 0:
        False
    if a + b + c == 2020:
        return True
    else:
        return False


def run2(items):
    for i in range(0, len(items)):
        for j in range(0, len(items)):
            for h in range(0, len(items)):
                if i == j or i == h or j == h:
                    continue
                a = items[i]
                b = items[j]
                c = items[h]
                if is_2020_3(a, b, c):
                    return a * b * c


def part2():
    with open('../inputs/input01') as input:
        print(run2([int(item.strip())
                    for item in input if not item.isspace()]))


def read_input():
    with open('input') as input:
        pass
    pass


class TestPart1(unittest.TestCase):
    def test_is_2020(self):
        self.assertEqual(is_2020(1721, 299), True)
        self.assertEqual(is_2020(0, 0), False)
        self.assertEqual(is_2020(-100, -1900), False)
        self.assertEqual(is_2020(100, 1900), False)

    def test_run(self):
        self.assertEqual(run([1721, 299]), 514579)
        self.assertEqual(run([0, 1, 1721, 2, 299]), 514579)


class TestPart2(unittest.TestCase):
    def test_is_2020_3(self):
        self.assertEqual(is_2020_3(979, 366, 675), True)
        self.assertEqual(is_2020_3(0, 1721, 299), True)

    def test_run2(self):
        self.assertEqual(run2([979, 366, 675]), 241861950)
        self.assertEqual(run2([0, 1, 979, 366, 675, -1, 3]), 241861950)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
