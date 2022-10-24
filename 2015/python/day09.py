import itertools
import sys


def parse_locations_distance(line):
    locations, distance = line.split('=')
    begin, end = locations.split(' to ')
    distance = int(distance.strip())

    return begin.strip(), end.strip(), distance


def part1(locations_distance_list):
    locations = set()
    distances = {}
    for locations_distance in locations_distance_list:
        begin, end, distance = locations_distance
        locations.add(begin)
        locations.add(end)
        distances[begin + ':' + end] = distance
        distances[end + ':' + begin] = distance
    product = itertools.permutations(locations, len(locations))
    max_travel = 0
    min_travel = sys.maxsize
    for p in product:
        i = 0
        c = 0
        while i < len(p) - 1:
            d = distances[p[i] + ':' + p[i + 1]]
            c += d
            i += 1
        if c < min_travel: min_travel = c
        if c > max_travel: max_travel = c
    print(min_travel)
    print(max_travel)


with open('inputs/input09') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]
    locations_distance_list = []
    for line in lines:
        locations_distance_list.append(parse_locations_distance(line))
    part1(locations_distance_list)
