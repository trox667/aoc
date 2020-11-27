import unittest

directions = {'(': 1, ')': -1}


def step(direction):
    count = directions.get(direction)
    if count:
        return count
    else:
        return 0


def run(path):
    return sum([step(s)for s in path])


def run2(path):
    total = 0
    i = 0
    for s in path:
        i = i+1
        total = total + step(s)
        if total == -1:
            break
    return i


def part1():
    with open('input01') as input:
        print(run(input.read().rstrip()))


def part2():
    with open('input01') as input:
        print(run2(input.read().rstrip()))


class Part1(unittest.TestCase):
    def test_step(self):
        self.assertEqual(step('9'), 0)
        self.assertEqual(step('('), 1)
        self.assertEqual(step(')'), -1)

    def test_run(self):
        self.assertEqual(run('(())'), 0)
        self.assertEqual(run('()()'), 0)
        self.assertEqual(run('((('), 3)
        self.assertEqual(run('(()(()('), 3)
        self.assertEqual(run('))((((('), 3)
        self.assertEqual(run('())'), -1)
        self.assertEqual(run('))('), -1)
        self.assertEqual(run(')))'), -3)
        self.assertEqual(run(')())())'), -3)


class Part2(unittest.TestCase):
    def test_run2(self):
        self.assertEqual(run2(')'), 1)
        self.assertEqual(run2('()())'), 5)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
