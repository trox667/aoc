import sys
from multiprocessing import Pool
from heapq import heappop, heappush

def dijkstra(start, end, heightmap):
	assert(start[0] != end[0] or start[1] != end[1])

	def to_hash(node):
		return f'{node[0]}:{node[1]}'

	heightmap[start[1]][start[0]] = ord('a')
	heightmap[end[1]][end[0]] = ord('z')

	queue = []
	queue.append((0, start))

	visited = []
	distances = {to_hash(start): 0}
	prev = {}

	for y in range(len(heightmap)):
		for x in range(len(heightmap[y])):
			if x == start[0] and y == start[1]:
				continue
			else:
				distances[to_hash([x, y])] = sys.maxsize
				prev[to_hash([x, y])] = None

	while queue:
		curr_value, curr = heappop(queue)
		height_value = heightmap[curr[1]][curr[0]]
		if curr in visited:
			continue
		visited.append(curr)

		options = []
		if curr[1]-1 >= 0:
			x,y = curr[0], curr[1]-1
			if heightmap[y][x]-height_value <= 1:
				options.append([x, y])
		if curr[1]+1 < len(heightmap):
			x,y = curr[0], curr[1]+1
			if heightmap[y][x]-height_value <= 1:
				options.append([x, y])
		if curr[0]-1 >= 0:
			x,y = curr[0]-1, curr[1]
			if heightmap[y][x]-height_value <= 1:
				options.append([x, y])
		if curr[0]+1 < len(heightmap[curr[1]]):
			x,y = curr[0]+1, curr[1]
			if heightmap[y][x]-height_value <= 1:
				options.append([x, y])

		for option in options:
			new_effort = curr_value + heightmap[option[1]][option[0]]
			if new_effort < distances[to_hash(option)]:
				heappush(queue, (new_effort, option))
				distances[to_hash(option)] = new_effort
				prev[to_hash(option)] = curr

	paths = []
	curr = end
	while curr != None:
		paths.insert(0, curr)
		curr = prev[to_hash(curr)] if to_hash(curr) in prev else None
		if curr == start:
			break

	return len(paths)


with open('../inputs/input12') as f:
# with open('./test12') as f:
	heightmap = [[ord(x) for x in line.strip()] for line in f.readlines() if len(line) > 0]

	start = [0, 0]
	end = [0, 0]
	for y in range(len(heightmap)):
		for x in range(len(heightmap[y])):
			if heightmap[y][x] == 83:
				start[0] = x
				start[1] = y
			elif heightmap[y][x] == 69:
				end[0] = x
				end[1] = y
	print('Part 1:', dijkstra(start, end, heightmap))

	starts = []
	for y in range(len(heightmap)):
		for x in range(len(heightmap[y])):
			if heightmap[y][x] == ord('a'):
				starts.append([x,y])
	
	p = Pool(1)
	print('Part 2:', min([x for x in p.starmap(dijkstra, [(start, end, heightmap) for start in starts]) if x > 1]))
