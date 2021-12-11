def load_file():
    with open('../inputs/input11') as file:
        return file.read()


def create_energy_map():
    data = load_file()
    return [[int(c) for c in line] for line in data.splitlines()]


def neighbors(x, y, width, height):
    n = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x, y),
         (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    return list(filter(lambda t: 0 <= t[0] < width and 0 <= t[1] < height, n))


def update(positions, energy_map, flashed):
    flash = []
    for x, y in positions:
        if (x, y) not in flashed:
            energy_map[y][x] += 1
            if energy_map[y][x] > 9:
                flash.append((x, y))
                energy_map[y][x] = 0
    return flash


def sum_is_zero(energy_map):
    for y in range(len(energy_map)):
        for x in range(len(energy_map[0])):
            if energy_map[y][x] > 0:
                return False
    return True


def run(steps, energy_map):
    width = len(energy_map[0])
    height = len(energy_map)
    positions = []
    for y in range(height):
        for x in range(width):
            positions.append((x, y))

    flash_counter = 0
    step_zero = None
    for step in range(steps):
        if sum_is_zero(energy_map):
            return None, step
        current_flashes = update(positions, energy_map, [])
        skip_flashes = set(current_flashes)
        flash_counter += len(current_flashes)
        while len(current_flashes) > 0:
            x, y = current_flashes.pop(0)
            n_flashes = update(neighbors(x, y, width, height), energy_map,
                               skip_flashes)
            flash_counter += len(n_flashes)
            skip_flashes.update(n_flashes)
            current_flashes.extend(n_flashes)

    return flash_counter, step_zero


def part1():
    return run(100, create_energy_map())[0]


def part2():
    return run(1000, create_energy_map())[1]


print(part1())
print(part2())
