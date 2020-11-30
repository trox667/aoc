import unittest


class PathData:
    def __init__(self):
        self.count = 0
        self.hits = set()
        self.trace = dict()

    def add_pos(self, pos):
        self.count += 1
        if not (pos in self.hits):
            key = '{0},{1}'.format(pos[0], pos[1])
            self.trace[key] = self.count
            self.hits.add(pos)


def draw_path(pos, path):
    curr_pos = pos
    data = PathData()
    for element in path:
        curr_pos = draw_element(data, curr_pos, element)
    return data


def draw_element(data, pos, element):
    px, py = pos
    direction, count = parse_element(element)
    if direction == 'U':
        for y in range(py+1, py+1+count):
            data.add_pos((px, y))
        return (px, py+count)
    elif direction == 'D':
        for y in range(py-1, py-1-count, -1):
            data.add_pos((px, y))
        return (px, py-count)
    elif direction == 'L':
        for x in range(px-1, px-1-count, -1):
            data.add_pos((x, py))
        return (px-count, py)
    elif direction == 'R':
        for x in range(px+1, px+1+count):
            data.add_pos((x, py))
        return (px+count, py)
    else:
        pass


def parse_element(element):
    direction, *count = element[0:]
    count = int(''.join(count))
    return (direction, count)


def mark_pos(hits, pos):
    hits.add(pos)


def manhattan_distance(pos):
    x, y = pos
    return abs(x) + abs(y)


def read_input():
    paths = []
    with open('input03') as input:
        paths = [path.rstrip().split(',') for path in input]
    return paths


def run(paths, part1=True):
    data_sets = []
    for path in paths:
        data = draw_path((0, 0), path)
        data_sets.append(data)
    if len(data_sets) >= 2:
        intersections = data_sets[0].hits.intersection(data_sets[1].hits)
        if part1:
            distances = [manhattan_distance(intersection)
                         for intersection in intersections]
            distances.sort()
            if len(distances) > 0:
                return distances[0]
        else:
            steps = list()
            for intersection in intersections:
                key = '{0},{1}'.format(intersection[0], intersection[1])
                a = data_sets[0].trace[key]
                b = data_sets[1].trace[key]
                steps.append(a+b)
            steps.sort()
            if len(steps) > 0:
                return steps[0]

    return 0


def part1():
    paths = read_input()
    return run(paths)


def part2():
    paths = read_input()
    return run(paths, False)


class TestPart1(unittest.TestCase):
    def test_run(self):
        paths = [
            ['R8', 'U5', 'L5', 'D3'],
            ['U7', 'R6', 'D4', 'L4']
        ]
        self.assertEqual(run(paths), 6)

        paths = [
            ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
            ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
        ]
        self.assertEqual(run(paths), 159)

        paths = [
            ['R98', 'U47', 'R26', 'D63', 'R33', 'U87',
                'L62', 'D20', 'R33', 'U53', 'R51'],
            ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
        ]
        self.assertEqual(run(paths), 135)


if __name__ == '__main__':
    print(part1())
    print(part2())
    unittest.main()
    pass
