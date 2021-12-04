test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def load_file():
    with open('../inputs/input04') as file:
        return file.read()


def file_to_input():
    lines = [line.strip() for line in load_file().splitlines() if line.strip()]
    # lines = [line.strip() for line in test.splitlines() if line.strip()]
    return lines[:1][0], lines[1:]


def get_board_input(lines):
    boards = []
    for i in range(0, len(lines), 5):
        boards.append(Board(lines[i:i + 5]))
    return boards


class Board:
    def __init__(self, lines):
        self.grid = []
        self.marker = set()
        self.last_marker = None
        self.completed = False

        for line in lines:
            row = []
            for word in line.split():
                row.append(int(word))
            self.grid.append(row)

    def mark(self, value):
        y = 0
        for row in self.grid:
            x = 0
            for v in row:
                if v == value:
                    self.marker.add((x, y))
                    self.last_marker = value
                x += 1
            y += 1

    def is_completed(self):
        for i in range(5):
            if (0, i) in self.marker and (1, i) in self.marker and (
                    2, i) in self.marker and (3, i) in self.marker and (
                    4, i) in self.marker:
                return True
            if (i, 0) in self.marker and (i, 1) in self.marker and (
                    i, 2) in self.marker and (i, 3) in self.marker and (
                    i, 4) in self.marker:
                return True
        return False

    def sum_unmarked(self):
        s = 0
        for y in range(5):
            for x in range(5):
                if (x, y) not in self.marker:
                    s += self.grid[y][x]
        return s


def part1():
    numbers, board_input = file_to_input()
    boards = get_board_input(board_input)
    for value in numbers.split(','):
        for board in boards:
            board.mark(int(value))
            if board.is_completed():
                return board.sum_unmarked() * board.last_marker


def part2():
    results = []
    numbers, board_input = file_to_input()
    boards = get_board_input(board_input)
    for value in numbers.split(','):
        for board in boards:
            if board.completed:
                continue
            board.mark(int(value))
            if board.is_completed():
                board.completed = True
                results.append(board.sum_unmarked() * board.last_marker)
    return results.pop()


print(part1())
print(part2())
