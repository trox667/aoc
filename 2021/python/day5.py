import re
from collections import defaultdict


class Line:
    def __init__(self, values):
        self.x1 = values[0]
        self.y1 = values[1]
        self.x2 = values[2]
        self.y2 = values[3]

    def range(self):
        x_incr = 1 if self.x1 <= self.x2 else -1
        y_incr = 1 if self.y1 <= self.y2 else -1
        return range(self.x1, self.x2 + x_incr, x_incr), range(self.y1,
                                                               self.y2 + y_incr,
                                                               y_incr)

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def is_diagonal(self):
        return abs(self.x1 - self.x2) == abs(self.y1 - self.y2)


def line_generator(lines, diagonal):
    for line in lines:
        x_range, y_range = line.range()
        if line.is_horizontal():
            for x in x_range:
                yield x, line.y1
        elif line.is_vertical():
            for y in y_range:
                yield line.x1, y
        elif diagonal and line.is_diagonal():
            for x, y in zip(x_range, y_range):
                yield x, y


def load_file():
    with open('../inputs/input05') as file:
        return file.read()


def file_to_lines():
    return [Line(list(map(int, line.replace('->', ',').split(',')))) for line
            in
            load_file().splitlines()]


def run(diagonal=False):
    visited = defaultdict(int)
    for coord in line_generator(file_to_lines(), diagonal):
        visited[coord] += 1
    return sum([1 for match in visited.values() if match > 1])


def part1():
    return run()


def part2():
    return run(True)


print(part1())
print(part2())
