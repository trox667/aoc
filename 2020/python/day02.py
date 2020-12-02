import unittest
import re


def parse(line):
    # use regex, credits to https://github.com/apaulheim :)
    matches = re.match(r'(\d+)-(\d+) ([A-z]): ([A-z]+)', line)
    assert matches
    return (matches.group(4), matches.group(3), (int(matches.group(1)), int(matches.group(2))))


def char_count(password, c):
    return password.count(c)


def policy_min_max(password, c, min_max):
    min_occ, max_occ = min_max
    return min_occ <= char_count(password, c) <= max_occ


def match_policy(entry, policy):
    password, c, r = entry
    return policy(password, c, r)


def run(entries, policy):
    result = 0
    for entry in entries:
        if (match_policy(entry, policy)):
            result += 1
    return result


def part1():
    print(run(read_input(), policy_min_max))


def char_pos(password, c, pos):
    return password[pos - 1] == c


def policy_position(password, c, positions):
    return char_pos(password, c, positions[0]) ^ char_pos(
        password, c, positions[1])


def part2():
    print(run(read_input(), policy_position))


def read_input():
    with open('../inputs/input02') as input:
        return [parse(i) for i in input if not i.isspace()]


class TestPart1(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse('1-3 a: abcde'), ('abcde', 'a', (1, 3)))

    def test_char_count(self):
        self.assertEqual(char_count('abcde', 'a'), 1)
        self.assertEqual(char_count('cdefg', 'b'), 0)
        self.assertEqual(char_count('ccccccccc', 'c'), 9)

    def test_match_policy(self):
        self.assertTrue(match_policy(('abcde', 'a', (1, 3)), policy_min_max))
        self.assertFalse(match_policy(('cdefg', 'b', (1, 3)), policy_min_max))
        self.assertTrue(
            match_policy(('ccccccccc', 'c', (2, 9)), policy_min_max))

    def test_run(self):
        self.assertEqual(
            run([('abcde', 'a', (1, 3)), ('cdefg', 'b', (1, 3)),
                 ('ccccccccc', 'c', (2, 9))], policy_min_max), 2)


class TestPart2(unittest.TestCase):
    def test_char_pos(self):
        self.assertTrue(char_pos('abcde', 'a', 1))
        self.assertFalse(char_pos('cdefg', 'b', 1))
        self.assertTrue(char_pos('ccccccccc', 'c', 2))

    def test_match_policy2(self):
        self.assertTrue(match_policy(('abcde', 'a', (1, 3)), policy_position))
        self.assertFalse(match_policy(('cdefg', 'b', (1, 3)), policy_position))
        self.assertFalse(
            match_policy(('ccccccccc', 'c', (2, 9)), policy_position))

    def test_run2(self):
        self.assertEqual(
            run([('abcde', 'a', (1, 3)), ('cdefg', 'b', (1, 3)),
                 ('ccccccccc', 'c', (2, 9))], policy_position), 1)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
