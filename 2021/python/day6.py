def load_file():
    with open('../inputs/input06') as file:
        return file.read()


def create_state():
    return list(map(int, load_file().split(',')))


def run(state, days=80):
    numbers = [0 for _ in range(9)]
    for s in state:
        numbers[s] += 1

    for day in range(0, days):
        count_new = numbers[0]
        numbers[0] = 0
        for i in range(1, 9):
            if numbers[i] > 0:
                numbers[i - 1] = numbers[i]
                numbers[i] = 0

        numbers[6] += count_new
        numbers[8] += count_new

    return sum(numbers)


def part1():
    return run(create_state())


def part2():
    return run(create_state(), 256)


print(part1())
print(part2())
