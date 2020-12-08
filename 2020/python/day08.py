import unittest
import copy


def read_input():
    with open('../inputs/input08') as input:
        return input.readlines()


def parse(line):
    tokens = line.strip().split(' ')
    return (tokens[0], int(tokens[1]))


def step(instructions, pointer, acc):
    (op, count) = instructions[pointer]
    if op == 'acc':
        return (pointer + 1, acc + count)
    elif op == 'jmp':
        return (pointer + count, acc)
    else:
        return (pointer + 1, acc)


def outofbounds(pointer, size):
    return pointer >= size


def run(instructions):
    visited = set()
    pointer = 0
    acc = 0
    while True:
        if pointer in visited:
            return ('infinite', acc)
        visited.add(pointer)
        (p, a) = step(instructions, pointer, acc)
        pointer = p
        acc = a
        if outofbounds(pointer, len(instructions)):
            return ('finished', acc)


def part1():
    (state, acc) = run([parse(line) for line in read_input()])
    assert (state == 'infinite')
    print(acc)


def replace_op(pointer, instructions):
    op, v = instructions[pointer]
    if 'nop' in op:
        instructions[pointer] = ('jmp', v)
    elif 'jmp' in op:
        instructions[pointer] = ('nop', v)


def run2(lines):
    instructions = [parse(line) for line in lines]
    for pointer in range(0, len(instructions)):
        curr_instructions = copy.deepcopy(instructions)
        replace_op(pointer, curr_instructions)
        (state, acc) = run(curr_instructions)
        if state == 'finished':
            return acc


def part2():
    print(run2(read_input()))


test_input = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


class TestPart1(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse(test_input.split('\n')[0]), ('nop', 0))
        self.assertEqual(parse(test_input.split('\n')[1]), ('acc', 1))
        self.assertEqual(parse(test_input.split('\n')[2]), ('jmp', 4))

    def test_step(self):
        instructions = [parse(line) for line in test_input.split('\n')]
        idx = 0
        acc = 0
        self.assertEqual(step(instructions, idx, acc), (1, 0))
        idx = 1
        acc = 0
        self.assertEqual(step(instructions, idx, acc), (2, 1))
        idx = 2
        acc = 1
        self.assertEqual(step(instructions, idx, acc), (6, 1))
        idx = 6
        acc = 1
        self.assertEqual(step(instructions, idx, acc), (7, 2))

    def test_run(self):
        self.assertEqual(run([parse(line) for line in test_input.split('\n')]),
                         ('infinite', 5))


class TestPart2(unittest.TestCase):
    def test_run2(self):
        self.assertEqual(run2(test_input.split('\n')), 8)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
