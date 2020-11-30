import copy
import unittest

ops = {
    1: 'ADD',
    2: 'MUL',
    99: 'HALT'
}

machine = {
    'READ': ['ADD', 'MUL', 'HALT'],
    'ADD': ['READ'],
    'MUL': ['READ'],
    'HALT': []
}


def read(intcode, index):
    op = intcode[index]
    op = ops[op]
    return (op, index)


def add(intcode, index):
    ia = intcode[index]
    ib = intcode[index+1]
    ic = intcode[index+2]
    intcode[ic] = intcode[ia] + intcode[ib]
    return ('READ', index+3)


def mul(intcode, index):
    ia = intcode[index]
    ib = intcode[index+1]
    ic = intcode[index+2]
    intcode[ic] = intcode[ia] * intcode[ib]
    return ('READ', index+3)


def run(intcode, start=0):
    state = 'READ'
    index = start
    while True:
        if state == 'READ':
            state, index = read(intcode, index)
            index = index+1
        elif state == 'ADD':
            state, index = add(intcode, index)
        elif state == 'MUL':
            state, index = mul(intcode, index)
        elif state == 'END':
            break
        else:
            break


def read_input():
    intcode = []
    with open('input02') as input:
        input = input.read()
        if len(input) > 0:
            intcode = [int(i) for i in input.split(',')]
    return intcode


def part1():
    intcode = read_input()
    intcode[1] = 12
    intcode[2] = 2
    run(intcode)
    return intcode[0]


def part2():
    target = 19690720
    intcode = read_input()
    for noun in range(0, 99):
        for verb in range(0, 99):
            curr_intcode = copy.deepcopy(intcode)
            curr_intcode[1] = noun
            curr_intcode[2] = verb
            run(curr_intcode)
            if curr_intcode[0] == target:
                return 100 * noun + verb


class TestDay2(unittest.TestCase):
    def test_add(self):
        intcode = [1, 0, 0, 3, 99]
        self.assertEqual(add(intcode, 1), ('READ', 4))
        self.assertEqual(intcode[3], 2)

    def test_mul(self):
        intcode = [1, 0, 3, 3, 99]
        self.assertEqual(mul(intcode, 1), ('READ', 4))
        self.assertEqual(intcode[3], 3)

    def test_run(self):
        intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        run(intcode, 0)
        self.assertEqual(intcode[0], 3500)
        intcode = [1, 0, 0, 0, 99]
        run(intcode, 0)
        self.assertEqual(intcode[0], 2)
        intcode = [2, 3, 0, 3, 99]
        run(intcode, 0)
        self.assertEqual(intcode[3], 6)
        intcode = [2, 4, 4, 5, 99, 0]
        run(intcode, 0)
        self.assertEqual(intcode[5], 9801)
        intcode = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        run(intcode, 0)
        self.assertEqual(intcode[0], 30)


if __name__ == '__main__':
    print(part1())
    print(part2())
    unittest.main()
    pass
