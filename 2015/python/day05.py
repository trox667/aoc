import unittest

vowels = 'aeiou'
forbidden = {'ab', 'cd', 'pq', 'xy'}


def letter_pair(text):
    for i in range(0, len(text)):
        if i < len(text)-1 and text[i] == text[i+1]:
            return True
    return False


def count_vowels(text):
    count = 0
    for v in vowels:
        count += text.count(v)
    return count


def no_forbidden_strings(text):
    is_not_forbidden = True
    for f in forbidden:
        if text.count(f) > 0:
            is_not_forbidden = False
            break
    return is_not_forbidden


def run(text):
    has_three_vowels = count_vowels(text) >= 3
    has_letter_pair = letter_pair(text)
    is_not_forbidden = no_forbidden_strings(text)
    return has_three_vowels and has_letter_pair and is_not_forbidden


def part1():
    with open('input05') as input:
        print(sum([run(text) for text in input if len(text)]))


def run2():
    pass


def part2():
    pass


def read_input():
    pass


class TestPart1(unittest.TestCase):
    def test_letter_pair(self):
        self.assertEqual(letter_pair('xyz'), False)
        self.assertEqual(letter_pair('xxz'), True)
        self.assertEqual(letter_pair('xxzz'), True)
        self.assertEqual(letter_pair('xxxzz'), True)
        self.assertEqual(letter_pair('xxxzzz'), True)

    def test_count_vowels(self):
        self.assertEqual(count_vowels('aaa'), 3)
        self.assertEqual(count_vowels(''), 0)
        self.assertEqual(count_vowels('xyz'), 0)
        self.assertEqual(count_vowels('abc'), 1)

    def test_no_forbidden_strings(self):
        self.assertEqual(no_forbidden_strings('abc'), False)
        self.assertEqual(no_forbidden_strings('acb'), True)

    def test_run(self):
        self.assertEqual(run('ugknbfddgicrmopn'), True)
        self.assertEqual(run('aaa'), True)
        self.assertEqual(run('jchzalrnumimnmhp'), False)
        self.assertEqual(run('haegwjzuvuyypxyu'), False)
        self.assertEqual(run('dvszwmarrgswjxmb'), False)
        pass


class TestPart2(unittest.TestCase):
    def test_run2(self):
        pass


if __name__ == '__main__':
    part1()
    unittest.main()
