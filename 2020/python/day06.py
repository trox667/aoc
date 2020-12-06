import unittest
import itertools


def parse(input: str):
    return [block.replace('\n', ' ').strip() for block in input.split('\n\n')]


def run(all_answers):
    count = 0
    for answers in all_answers:
        answers = "".join(answers).replace(' ', '')
        unique_keys = [set(l) for l in answers]
        count += len(unique_keys[0].union(*unique_keys[1:]))
    return count


def part1():
    print(run(parse(read_input())))


def run2(all_answers):
    count = 0
    for answers in all_answers:
        people_answers = answers.split(' ')
        unique_keys = [set(l) for l in people_answers]
        count += len(unique_keys[0].intersection(*unique_keys[1:]))

    return count


def part2():
    print(run2(parse(read_input())))


def read_input():
    with open('../inputs/input06') as input:
        return input.read()


test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""


class TestPart1(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse(test_input),
                         ['abc', 'a b c', 'ab ac', 'a a a a', 'b'])

    def test_run(self):
        self.assertEqual(run(parse(test_input)), 11)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        self.assertEqual(run2(parse(test_input)), 6)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
    pass
