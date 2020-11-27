import unittest

directions = {'^': (0, 1), '<': (-1, 0), '>': (1, 0), 'v': (0, -1)}


class TraceData:
    def __init__(self):
        self.trace = {(0, 0)}
        self.position = (0, 0)

    def add(self, position):
        cx, cy = self.position
        x, y = position
        self.position = (cx + x, cy + y)
        self.trace.add(self.position)


def direction(d):
    d = directions.get(d)
    if d:
        return d
    else:
        return (0, 0)


def move(data, increment):
    data.add(increment)


def run(path):
    data = TraceData()
    for i in path:
        move(data, direction(i))

    return len(data.trace)


def part1():
    with open('input03') as input:
        print(run(input.read()))


def run2(path):
    path = list(path)
    path_a = path[::2]
    path.pop(0)
    path_b = path[::2]
    data = TraceData()
    for i in path_a:
        move(data, direction(i))
    data.position = (0, 0)
    for i in path_b:
        move(data, direction(i))
    return len(data.trace)


def part2():
    with open('input03') as input:
        print(run2(input.read()))


class Test1(unittest.TestCase):
    def test_move(self):
        data = TraceData()
        move(data, (1, 0))
        self.assertEqual(data.trace.pop(), (1, 0))

    def test_direction(self):
        self.assertEqual(direction('^'), (0, 1))
        self.assertEqual(direction('v'), (0, -1))
        self.assertEqual(direction('<'), (-1, 0))
        self.assertEqual(direction('>'), (1, 0))
        self.assertEqual(direction(''), (0, 0))

    def test_run(self):
        self.assertEqual(run('>'), 2)
        self.assertEqual(run('^>v<'), 4)
        self.assertEqual(run('^v^v^v^v^v'), 2)


class Test2(unittest.TestCase):
    def test_run2(self):
        self.assertEqual(run2('^v'), 3)
        self.assertEqual(run2('^>v<'), 3)
        self.assertEqual(run2('^v^v^v^v^v'), 11)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
