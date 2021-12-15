import sys
from collections import defaultdict
from queue import PriorityQueue


def load_file():
    with open('../inputs/input15') as file:
        return file.read()


def build_grid():
    data = load_file().splitlines()
    grid = []
    y = 0
    for line in data:
        row = []
        x = 0
        for col in line:
            row.append(int(col))
            x += 1
        grid.append(row)
        y += 1
    return grid


def build_grid2():
    data = load_file().splitlines()
    grid = []
    y = 0
    for line in data:
        row = []
        x = 0
        for col in line:
            row.append(int(col))
            x += 1

        curr_row = row
        for i in range(1, 5):
            prev_row = curr_row.copy()
            curr_row = []
            for col in prev_row:
                val = 1 if col + 1 > 9 else col + 1
                curr_row.append(val)
                x += 1
            row.extend(curr_row)

        grid.append(row)
        y += 1

    height = len(grid)

    for i in range(1, 5):
        s = (i - 1) * height  # 0,10 10,20 20,30 30,40
        e = i * height
        rows = grid[s:e]
        for row in rows:
            curr_row = []
            for col in row:
                val = 1 if col + 1 > 9 else col + 1
                curr_row.append(val)
            grid.append(curr_row)

    return grid


def index(x, y, width):
    return y * width + x


def position(idx, width):
    return idx % width, idx // width


def get_neighbors(x, y, width, height):
    n = []
    if x - 1 >= 0:
        n.append((x - 1, y))
    if x + 1 < width:
        n.append((x + 1, y))
    if y - 1 >= 0:
        n.append((x, y - 1))
    if y + 1 < height:
        n.append((x, y + 1))
    return n


def build_graph(grid):
    height = len(grid)
    width = len(grid[0])
    graph = defaultdict(list)
    for y in range(0, height):
        for x in range(0, width):
            node_from = index(x, y, width)
            neighbors = get_neighbors(x, y, width, height)
            for n in neighbors:
                node_to = index(n[0], n[1], width)
                value = grid[n[1]][n[0]]
                graph[node_from].append((node_to, value))
    return graph


def dijkstra(start, end, graph):
    node_count = len(graph)
    distances = [sys.maxsize for _ in range(node_count)]
    distances[start] = 0
    visited = [False for _ in range(node_count)]

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        _, node = pq.get()
        if visited[node]:
            continue
        visited[node] = True
        for neighbor, distance in graph[node]:
            total_dist = distances[node] + distance
            if total_dist < distances[neighbor]:
                distances[neighbor] = total_dist
                pq.put((distances[neighbor], neighbor))
    return distances[end]


def part1():
    grid = build_grid()
    graph = build_graph(grid)
    height = len(grid)
    width = len(grid[0])
    start = index(0, 0, width)
    end = index(width - 1, height - 1, width)
    return dijkstra(start, end, graph)


def part2():
    grid = build_grid2()
    graph = build_graph(grid)
    height = len(grid)
    width = len(grid[0])
    start = index(0, 0, width)
    end = index(width - 1, height - 1, width)
    return dijkstra(start, end, graph)


print(part1())
print(part2())
