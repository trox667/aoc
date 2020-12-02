import unittest


def parse(line):
    r, c, password = line.split(' ')
    rs, re = r.split('-')
    c, *tail = c.split(':')
    return (password, c, (int(rs), int(re)))


def char_count(password, c):
    return password.count(c)


def match_policy(password, c, occurences):
    min_occ, max_occ = occurences
    count = char_count(password, c)
    return min_occ <= count <= max_occ


def run(entries):
    result = 0
    for entry in entries:
        password, c, occurences = entry
        if (match_policy(password, c, occurences)):
            result += 1
    return result


def part1():
    print(run(read_input()))


def char_pos(password, c, pos):
    return password[pos - 1] == c


def match_policy2(password, c, positions):
    return char_pos(password, c, positions[0]) ^ char_pos(
        password, c, positions[1])


def run2(entries):
    result = 0
    for entry in entries:
        password, c, occurences = entry
        if (match_policy2(password, c, occurences)):
            result += 1
    return result


def part2():
    print(run2(read_input()))


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
        self.assertTrue(match_policy('abcde', 'a', (1, 3)))
        self.assertFalse(match_policy('cdefg', 'b', (1, 3)))
        self.assertTrue(match_policy('ccccccccc', 'c', (2, 9)))

    def test_run(self):
        self.assertEqual(
            run([('abcde', 'a', (1, 3)), ('cdefg', 'b', (1, 3)),
                 ('ccccccccc', 'c', (2, 9))]), 2)


class TestPart2(unittest.TestCase):
    def test_char_pos(self):
        self.assertTrue(char_pos('abcde', 'a', 1))
        self.assertFalse(char_pos('cdefg', 'b', 1))
        self.assertTrue(char_pos('ccccccccc', 'c', 2))

    def test_match_policy2(self):
        self.assertTrue(match_policy2('abcde', 'a', (1, 3)))
        self.assertFalse(match_policy2('cdefg', 'b', (1, 3)))
        self.assertFalse(match_policy2('ccccccccc', 'c', (2, 9)))

    def test_run2(self):
        self.assertEqual(
            run2([('abcde', 'a', (1, 3)), ('cdefg', 'b', (1, 3)),
                  ('ccccccccc', 'c', (2, 9))]), 1)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
    pass
