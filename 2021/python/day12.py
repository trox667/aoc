from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.paths = []
        self.current_path = []
        self.visited = defaultdict(int)
        self.abort = lambda v, n: v[n] == 1

    def add_edge(self, a, b):
        self.graph[a].append(b)

    # https://www.baeldung.com/cs/simple-paths-between-two-vertices
    def dfs(self, start, end):
        if self.abort(self.visited, start):
            return
        if start.islower():
            self.visited[start] += 1
        self.current_path.append(start)
        if start == end:
            self.paths.append(self.current_path.copy())
            self.visited[start] -= 1
            self.current_path.pop()
            return
        for neighbor in self.graph[start]:
            self.dfs(neighbor, end)
        self.current_path.pop()
        self.visited[start] -= 1


def load_file():
    with open('../inputs/input12') as file:
        return file.read()


def create_graph():
    data = load_file()
    graph = Graph()
    for line in data.splitlines():
        a, b = line.split('-')
        graph.add_edge(a, b)
        graph.add_edge(b, a)
    return graph


def part1():
    graph = create_graph()
    graph.dfs('start', 'end')
    return len(graph.paths)


def part2():
    def abort(visited, node):
        visited_twice = sum([1 for v in visited.values() if v >= 2])
        if visited_twice:
            if visited[node] >= 1:
                return True
        elif node in ['start', 'end'] and visited[node] >= 1:
            return True
        return False

    graph = create_graph()
    graph.abort = abort
    graph.dfs('start', 'end')
    return len(graph.paths)


print(part1())  # 4549
print(part2())  # 120535
