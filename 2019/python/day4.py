
import unittest


def split_number(n):
    return [int(i) for i in str(n)]


def count_occurence(list, n):
    return list.count(n)


def has_double_rule(list):
    for i in range(0, 9+1):
        count = count_occurence(list, i)
        if count == 2:
            return True
    return False


def has_neighbor_rule(list):
    for i in range(1, len(list)):
        if list[i-1] == list[i]:
            return True
    return False


def never_decrease_rule(list):
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            return False
    return True


def combined_rules(list):
    return never_decrease_rule(list) and has_neighbor_rule(list)


def combined_rules2(list):
    return never_decrease_rule(list) and has_double_rule(list)


def create_variants(start, end):
    r = range(start, end)
    return [split_number(i) for i in r]


def part1():
    variants = create_variants(168630, 718098)
    options = [i for i in filter(combined_rules, variants)]
    return len(options)


def part2():
    variants = create_variants(168630, 718098)
    options = [i for i in filter(combined_rules2, variants)]
    return len(options)


class TestPart1(unittest.TestCase):
    def test_neighbor_rule(self):
        self.assertEqual(has_neighbor_rule([1, 2, 3, 4]), False)
        self.assertEqual(has_neighbor_rule([1, 1, 3, 4]), True)
        self.assertEqual(has_neighbor_rule([1, 2, 2, 4]), True)
        self.assertEqual(has_neighbor_rule([1, 2, 3, 3]), True)
        self.assertEqual(has_neighbor_rule([4, 3, 2, 2]), True)

    def test_never_decrease_rule(self):
        self.assertEqual(never_decrease_rule([1, 2, 3, 4]), True)
        self.assertEqual(never_decrease_rule([1, 2, 3, 3]), True)
        self.assertEqual(never_decrease_rule([1, 2, 3, 1]), False)

    def test_split_number(self):
        self.assertEqual(split_number(1234), [1, 2, 3, 4])


class TestPart2(unittest.TestCase):
    def test_occurence(self):
        self.assertEqual(count_occurence([1, 2, 3, 2, 1], 1), 2)
        self.assertEqual(count_occurence([1, 2, 3, 2, 1], 2), 2)
        self.assertEqual(count_occurence([1, 2, 3, 2, 1], 3), 1)
        self.assertEqual(count_occurence([1, 2, 3, 2, 1], 4), 0)

    def test_double_rule(self):
        self.assertEqual(has_double_rule([1, 1, 2, 2, 3, 3]), True)
        self.assertEqual(has_double_rule([1, 2, 3, 4, 4, 4]), False)
        self.assertEqual(has_double_rule([1, 1, 1, 1, 2, 2]), True)
        self.assertEqual(has_double_rule([1, 1, 1, 1, 1, 1]), False)


if __name__ == '__main__':
    print(part1())
    print(part2())
    unittest.main()
