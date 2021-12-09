import sys

test = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def load_file():
    with open('../inputs/input09') as file:
        return file.read()


def heightmap_from_file():
    # file_input = test
    file_input = load_file()
    return [int(c) for line in file_input.splitlines() for c in line], len(
        file_input.splitlines()[0])


def index(x, y, width):
    return y * width + x


def position(idx, width):
    return idx % width, idx // width


def walk_map(heightmap, width):
    marked = set()
    h = len(heightmap) // width
    for i in range(0, len(heightmap)):
        x, y = position(i, width)
        height = heightmap[i]
        if height == 9:
            continue

        neighbors = []
        if x - 1 >= 0:
            neighbors.append(index(x - 1, y, width))
        if x + 1 < width:
            neighbors.append(index(x + 1, y, width))
        if y - 1 >= 0:
            neighbors.append(index(x, y - 1, width))
        if y + 1 < h:
            neighbors.append(index(x, y + 1, width))

        mn = sys.maxsize
        for n in neighbors:
            mn = min(heightmap[n], mn)

        if height < mn:
            marked.add(i)

    return marked


def walk_map2(idx, heightmap, width, h, visited):
    x, y = position(idx, width)
    height = heightmap[idx]
    if height == 9:
        return

    visited.add(idx)

    neighbors = []
    if x - 1 >= 0:
        neighbors.append(index(x - 1, y, width))
    if x + 1 < width:
        neighbors.append(index(x + 1, y, width))
    if y - 1 >= 0:
        neighbors.append(index(x, y - 1, width))
    if y + 1 < h:
        neighbors.append(index(x, y + 1, width))

    for n in neighbors:
        if n not in visited and heightmap[n] != 9:
            walk_map2(n, heightmap, width, h, visited)

    pass


def part1():
    heightmap, width = heightmap_from_file()
    marked = walk_map(heightmap, width)
    sum = 0
    for m in marked:
        sum += heightmap[m] + 1
    return sum


def part2():
    results = []
    heightmap, width = heightmap_from_file()
    height = len(heightmap) // width
    for idx in range(0, len(heightmap)):
        visited = set()
        walk_map2(idx, heightmap, width, height, visited)
        tmp = []
        for v in visited:
            tmp.append(heightmap[v])
        if tmp not in results:
            results.append(tmp)

    results.sort(key=len)
    sum = 1
    for r in results[-3:]:
        sum *= len(r)
        print(r, len(r))
    print(sum)

print(part1())
print(part2())
