from functools import reduce


def load_file():
    with open('../inputs/input09') as file:
        return file.read()


def heightmap_from_file():
    file_input = load_file()
    return [int(c) for line in file_input.splitlines() for c in line], len(
        file_input.splitlines()[0])


def index(x, y, width):
    return y * width + x


def position(idx, width):
    return idx % width, idx // width


def neighbors(x, y, width, height):
    n = []
    if x - 1 >= 0:
        n.append(index(x - 1, y, width))
    if x + 1 < width:
        n.append(index(x + 1, y, width))
    if y - 1 >= 0:
        n.append(index(x, y - 1, width))
    if y + 1 < height:
        n.append(index(x, y + 1, width))
    return n


def get_low_points(heightmap, total_width):
    marked = set()
    total_height = len(heightmap) // total_width
    for i in range(0, len(heightmap)):
        x, y = position(i, total_width)
        height = heightmap[i]
        if height == 9:
            continue

        if height < min(
                [heightmap[n] for n in neighbors(x, y, total_width, total_height)]):
            marked.add(i)

    return marked


def get_basin(idx, heightmap, total_width, total_height, basin, visited):
    visited.add(idx)
    x, y = position(idx, total_width)
    height = heightmap[idx]
    if height == 9:
        return

    basin.add(idx)

    for n in neighbors(x, y, total_width, total_height):
        if n not in visited and heightmap[n] != 9:
            get_basin(n, heightmap, total_width, total_height, basin, visited)


def part1():
    heightmap, width = heightmap_from_file()
    marked = get_low_points(heightmap, width)
    return sum([heightmap[m] + 1 for m in marked])


def part2():
    results = []
    heightmap, width = heightmap_from_file()
    height = len(heightmap) // width
    visited = set()
    for idx in get_low_points(heightmap, width):
        basin = set()
        get_basin(idx, heightmap, width, height, basin, visited)
        results.append(basin)

    results.sort(key=len)
    return reduce(lambda a, b: a * b, [len(r) for r in results[-3:]], 1)


print(part1())
print(part2())
