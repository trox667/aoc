def load_file():
    with open('../inputs/input04') as file:
        return file.read()


def file_to_input():
    lines = [line.strip() for line in load_file().splitlines() if line.strip()]
    return map(int, lines[:1][0].split(',')), lines[1:]


def get_board_input(lines):
    boards = []
    for i in range(0, len(lines), 5):
        boards.append(Board(lines[i:i + 5]))
    return boards


def position_generator():
    """Provide a continuous list of x,y pairs from 0-5"""
    for i in range(25):
        x = i % 5
        y = i // 5
        yield x, y


class Board:
    def __init__(self, lines):
        self.marker = set()
        self.last_marker = None
        self.completed = False
        self.grid = [[int(word) for word in line.split()] for line in lines]

    def mark(self, value):
        """Mark the given `value` on the game board as found"""
        position = position_generator()
        for x, y in position:
            if self.grid[y][x] == value:
                self.marker.add((x, y))
                self.last_marker = value

    def is_completed(self):
        """Returns True if a row or column has five marked values"""
        for i in range(5):
            if {(0, i), (1, i), (2, i), (3, i), (4, i)}.issubset(
                    self.marker) or {(i, 0), (i, 1), (i, 2), (i, 3),
                                     (i, 4)}.issubset(self.marker):
                self.completed = True
                return self.completed
        return False

    def sum_unmarked(self):
        """Calculate the sum of all unmarked values on the board"""
        position = position_generator()
        return sum(
            [self.grid[y][x] for x, y in position if (x, y) not in self.marker])

    def result(self):
        """Return the result of the sum of all unmarked values
           multiplied by the last marked value"""
        return self.sum_unmarked() * self.last_marker


class Game:
    def __init__(self, numbers, boards):
        self.numbers = numbers
        self.boards = boards

    def run(self, exit_early=True):
        """Start the game and get the first result if `exit_early` is True.
           If `exit_early` is False it will return the last result"""
        results = []
        for number in self.numbers:
            for board in self.boards:
                if board.completed:
                    continue
                board.mark(number)
                if board.is_completed():
                    if exit_early:
                        return board.result()
                    else:
                        results.append(board.result())
        return results.pop()


def part1():
    numbers, board_input = file_to_input()
    game = Game(numbers, get_board_input(board_input))
    return game.run()


def part2():
    numbers, board_input = file_to_input()
    boards = get_board_input(board_input)
    game = Game(numbers, boards)
    return game.run(False)


print(part1())
print(part2())
