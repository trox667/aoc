test_depth = [199,
              200,
              208,
              210,
              200,
              207,
              240,
              269,
              260,
              263]


def load_file():
    with open('../inputs/input01') as file:
        return file.read()


def file_to_depths():
    return [int(line.strip()) for line in load_file().splitlines() if
            line.strip()]


def count_increasing(depths, start=1):
    return sum([depths[i - start] < depths[i] for i in
                range(start, len(depths))])


def part1():
    return count_increasing(file_to_depths())


def part2():
    return count_increasing(file_to_depths(), 3)


depths = file_to_depths()
print(part1())  # 1681
print(part2())  # 1704
