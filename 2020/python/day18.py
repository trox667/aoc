import unittest


def calc_inner(line: str):
    stack = []
    for token in line.split(' '):
        if token in ['*', '+']:
            stack.append(token)
        else:
            stack.append(int(token))
    stack.reverse()
    while len(stack) >= 3:
        b = stack.pop()
        op = stack.pop()
        a = stack.pop()
        if op == '+':
            stack.append(a+b)
        elif op == '*':
            stack.append(a*b)

    assert len(stack) == 1
    return stack[-1]


def run(line: str):
    while line.rfind('(') != -1 or len(line) > 0:
        start = line.rfind('(')
        end = line.find(')', start)
        if end == -1:
            return calc_inner(line)
        else:
            subs = line[start+1:end]
            line = line.replace(line[start:end+1], str(calc_inner(subs)))


def part1():
    print(sum([run(line) for line in read_input()]))


def calc_inner2(line: str):
    stack = []
    for token in line.split(' '):
        if token in ['*', '+']:
            stack.append(token)
        else:
            stack.append(int(token))
    stack.reverse()
    while len(stack) >= 3:
        i = 0
        while '+' in stack:
            if stack[i-1] == '+':
                b = stack.pop(i)
                op = stack.pop(i-1)
                a = stack.pop(i-2)
                stack.insert(i-2, a+b)
                i = 0
            i += 1
        i = 0
        while '*' in stack:
            if stack[i-1] == '*':
                b = stack.pop(i)
                op = stack.pop(i-1)
                a = stack.pop(i-2)
                stack.insert(i-2, a*b)
                i = 0
            i += 1

    assert len(stack) == 1
    return stack[-1]


def run2(line: str):
    while line.rfind('(') != -1 or len(line) > 0:
        start = line.rfind('(')
        end = line.find(')', start)
        if end == -1:
            return calc_inner2(line)
        else:
            subs = line[start+1:end]
            line = line.replace(line[start:end+1], str(calc_inner2(subs)))


def part2():
    print(sum([run2(line) for line in read_input()]))


def read_input():
    with open('../inputs/input18') as input:
        return [line for line in input if not line.isspace()]


class TestPart1(unittest.TestCase):
    def test_run(self):
        # run('1 + (2 * 3) + (4 * (5 + 6))')
        self.assertEqual(run('1 + 2 * 3 + 4 * 5 + 6'), 71)
        self.assertEqual(run('1 + (2 * 3) + (4 * (5 + 6))'), 51)
        self.assertEqual(run('2 * 3 + (4 * 5)'), 26)
        self.assertEqual(run('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 437)
        self.assertEqual(
            run('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 12240)
        self.assertEqual(
            run('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 13632)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        # run2('2 * 3 + (4 * 5)')
        self.assertEqual(run2('1 + (2 * 3) + (4 * (5 + 6))'), 51)
        self.assertEqual(run2('2 * 3 + (4 * 5)'), 46)
        self.assertEqual(run2('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 1445)
        self.assertEqual(
            run2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 669060)
        self.assertEqual(
            run2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 23340)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
