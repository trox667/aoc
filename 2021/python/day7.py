import sys


def load_file():
    with open('../inputs/input07') as file:
        return file.read()


def create_input():
    return [int(t) for t in load_file().split(',')]


def run(h_positions, calc_fuel=lambda d: d):
    last_pos = max(h_positions)
    min_fuel = sys.maxsize
    fuel_distance = {}
    for target_pos in range(last_pos):
        fuel = 0
        for crab_pos in h_positions:
            if target_pos == crab_pos:
                continue

            d = abs(crab_pos - target_pos)
            if d not in fuel_distance:
                fuel_req = calc_fuel(d)
                fuel_distance[d] = fuel_req
            fuel += fuel_distance[d]

            if fuel > min_fuel:
                break
        min_fuel = min(fuel, min_fuel)
    return min_fuel


def part1():
    return run(create_input())


def part2():
    return run(create_input(), lambda d: (d ** 2 + d) // 2)


print(part1())
print(part2())
