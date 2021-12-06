from collections import defaultdict

test = "3,4,3,1,2"


def load_file():
    with open('../inputs/input06') as file:
        return file.read()


def create_state():
    return list(map(int, load_file().split(',')))
    # return list(map(int, test.split(',')))


def run(state, days=80):
    d = defaultdict(int)
    for s in state:
        d[s] += 1

    for day in range(0, days):
        # how many new entries
        # how many need to be set to 6
        count_new = d[0]
        # all 0 handled
        d[0] = 0
        # decrement from values from 1-8
        for i in range(1, 9):
            if d[i] > 0:
                d[i - 1] = d[i]
                d[i] = 0

        # reset 0 to 6 and add new ones
        d[6] += count_new
        d[8] += count_new

    s = 0
    for v in d.values():
        s += v

    return s


def part1():
    return run(create_state())


def part2():
    return run(create_state(), 256)


print(part1())
print(part2())
