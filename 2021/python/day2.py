test = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]


def load_file():
    with open('../inputs/input02') as file:
        return file.read()


def file_to_commands():
    return [(line.strip().split(' ')[0], int(line.strip().split(' ')[1])) for
            line
            in load_file().splitlines() if
            line.strip()]


def part1():
    actions = {'forward': lambda x, y, step: (x + step, y),
               'down': lambda x, y, step: (x, y + step),
               'up': lambda x, y, step: (x, y - step)}
    x, y = 0, 0
    for (command, step) in file_to_commands():
        x, y = actions[command](x, y, step)
    return x * y


def part2():
    actions = {
        'forward': lambda x, y, step, aim: (x + step, y + step * aim, aim),
        'down': lambda x, y, step, aim: (x, y, aim + step),
        'up': lambda x, y, step, aim: (x, y, aim - step)}
    x, y, aim = 0, 0, 0
    for (command, step) in file_to_commands():
        x, y, aim = actions[command](x, y, step, aim)
    return x * y


print(part1())
print(part2())
