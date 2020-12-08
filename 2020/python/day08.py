import unittest
import copy


def parse(line):
    op, count = line.strip().split(' ')
    count = int(count)
    return (op, count)


def step(program, idx, acc):
    (op, count) = program[idx]
    if op == 'acc':
        acc += count
        idx += 1
    elif op == 'jmp':
        idx += count
    else:
        idx += 1
    return (idx, acc)


def run(lines):
    visited = set()
    program = [parse(line) for line in lines]
    idx = 0
    acc = 0
    while True:
        if idx in visited:
            return acc
        visited.add(idx)
        (i, a) = step(program, idx, acc)
        idx = i
        acc = a


def part1():
    print(run(read_input()))


def terminate_ok(idx, program):
    if idx >= len(program):
        return True
    else:
        return False


def run2(lines):
    program = [parse(line) for line in lines]
    for pointer in range(0, len(program)):
        curr_program = copy.deepcopy(program)
        op, v = curr_program[pointer]
        if 'nop' in op:
            curr_program[pointer] = ('jmp', v)
        elif 'jmp' in op:
            curr_program[pointer] = ('nop', v)

        visited_jumped = set()
        idx = 0
        acc = 0
        while True:
            if 'jmp' in curr_program[idx]:
                if idx in visited_jumped:
                    break
                else:
                    visited_jumped.add(idx)
            (i, a) = step(curr_program, idx, acc)
            idx = i
            acc = a
            if terminate_ok(idx, curr_program):
                return acc


def part2():
    print(run2(read_input()))


def read_input():
    with open('../inputs/input08') as input:
        return input.readlines()


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
        program = [parse(line) for line in test_input.split('\n')]
        idx = 0
        acc = 0
        self.assertEqual(step(program, idx, acc), (1, 0))
        idx = 1
        acc = 0
        self.assertEqual(step(program, idx, acc), (2, 1))
        idx = 2
        acc = 1
        self.assertEqual(step(program, idx, acc), (6, 1))
        idx = 6
        acc = 1
        self.assertEqual(step(program, idx, acc), (7, 2))

    def test_run(self):
        self.assertEqual(run(test_input.split('\n')), 5)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        self.assertEqual(run2(test_input.split('\n')), 8)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
