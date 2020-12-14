import unittest
import re

pattern = r"\[(?P<index>\d+)\] = (?P<value>\d+)"


def parse(line: str):
    if line.startswith('mask'):
        _, value = line.split(' = ')
        bit_and = value[value.index('1'):].replace('X', '1')
        bit_or = value[value.index('1'):].replace('X', '0')
        return (bit_and, bit_or, None, None)
    else:
        matches = re.search(pattern, line)
        index = int(matches.group('index'))
        value = int(matches.group('value'))
        return (None, None, index, value)


def run(instructions):
    bit_and = 0
    bit_or = 0
    mem = dict()
    for instruction in instructions:
        if instruction[0] != None and instruction[1] != None:
            bit_and = int(instruction[0], 2)
            bit_or = int(instruction[1], 2)
        else:
            index = instruction[2]
            value = instruction[3]
            mem[index] = value & bit_and | bit_or

    return sum(mem.values())


def part1():
    instructions = [parse(line) for line in read_input()]
    print(run(instructions))


def run2():
    pass


def part2():
    pass


def read_input():
    with open('../inputs/input14') as input:
        return [line for line in input if not line.isspace()]


test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


class TestPart1(unittest.TestCase):
    def test_parse(self):
        instructions = [
            parse(line) for line in test_input.split('\n')
            if not line.isspace()
        ]
        self.assertEqual(instructions, [('1111101', '1000000', None, None),
                                        (None, None, 8, 11),
                                        (None, None, 7, 101),
                                        (None, None, 8, 0)])

    def test_run(self):
        instructions = [
            parse(line) for line in test_input.split('\n')
            if not line.isspace()
        ]
        self.assertEqual(run(instructions), 165)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        pass


if __name__ == '__main__':
    part1()
    unittest.main()
