import unittest
import re
import itertools


def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString


pattern = r"\[(?P<index>\d+)\] = (?P<value>\d+)"


def parse(line: str):
    line = line.strip()
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


def prepend(i):
    s = bin(i)[2:]
    t = ''
    for i in range(0, 36-len(s)):
        t += '0'

    t += s
    return t


def create_combination(i, s):
    # assemble the result string value + mask
    p = list(prepend(i))
    assert len(p) == len(s)
    for i in range(0, len(p)):
        b = s[i]
        if b == '1':
            p[i] = '1'
        elif b == 'X':
            p[i] = 'X'
    s = ''.join(p)
    S = set()
    xs = s.count('X')
    perms = force(xs)

    # replace all X with permutations
    S = set()
    for p in perms:
        t = s
        P = list(p)
        for i in range(0, len(P)):
            t = replacenth(t, 'X', P[i], 1)
        S.add(t)

    return [int(s, 2) for s in S]


def force(l):
    return [seq for seq in itertools.product("01", repeat=l)]


def parse2(line: str):
    line = line.strip()
    if line.startswith('mask'):
        _, value = line.split(' = ')
        return (value, None, None)
    else:
        matches = re.search(pattern, line)
        index = int(matches.group('index'))
        value = int(matches.group('value'))
        return (None, index, value)


def run2(instructions):
    mem = dict()
    mask = ''
    for instruction in instructions:
        if instruction[0] != None:
            mask = instruction[0]
        else:
            index = instruction[1]
            value = instruction[2]
            for c in create_combination(index, mask):
                mem[c] = value

    return sum(mem.values())


def part2():
    instructions = [parse2(line) for line in read_input()]
    print(run2(instructions))


def read_input():
    with open('../inputs/input14') as input:
        return [line for line in input if not line.isspace()]


test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

test_input2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


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
        instructions = [parse2(line) for line in test_input2.split(
            '\n') if not line.isspace()]
        self.assertEqual(run2(instructions), 208)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
