def load_file():
    with open('../inputs/input13') as file:
        return file.read()


def get_coords_instructions():
    data = load_file()
    coords, instructions = [], []
    for line in data.splitlines():
        if line.strip():
            if line.startswith('fold'):
                instructions.append(
                    ('y', int(line.split('=')[1])) if 'y' in line else (
                        'x', int(line.split('=')[1])))
            else:
                coords.append(
                    (int(line.split(',')[0]), int(line.split(',')[1])))
    return coords, instructions


def print_coords(coords):
    for y in range(max(coords, key=lambda t: t[1])[1] + 1):
        for x in range(max(coords, key=lambda t: t[0])[0] + 1):
            print('#' if (x, y) in coords else '.', end='')
        print()


def fold(direction, value, coords):
    return set([(value - abs(x - value) if direction == 'x' else x,
                 value - abs(y - value) if direction == 'y' else y) for
                (x, y) in set(coords)])


def run(iterate_all=True):
    coords, instructions = get_coords_instructions()
    for direction, value in instructions:
        coords = fold(direction, value, coords)
        if not iterate_all:
            break
    return coords


def part1():
    return len(run(False))


def part2():
    return run()


print(part1())
print_coords(part2())
