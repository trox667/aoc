import sys
from multiprocessing import Pool

def dijkstra(start, end, heightmap):
	assert(start[0] != end[0] or start[1] != end[1])

	heightmap[start[1]][start[0]] = ord('a')
	heightmap[end[1]][end[0]] = ord('z')

	queue = []
	queue.append(start)

	for y in range(len(heightmap)):
		for x in range(len(heightmap[y])):
			if x == start[0] and y == start[1]:
				continue
			else:
				queue.append([x, y, sys.maxsize, None])

	visited = []

	def update_queue(queue):
		return sorted(queue, key=lambda item: item[2])

	paths = []
	def path(node):
		for v in visited:
			if v[0] == node[0] and v[1] == node[1]:
				prev = v[3]
				if prev != None:
					paths.append(prev)
					path(prev)


	while len(queue) > 0:
		curr_position = queue.pop(0)
		height_value = heightmap[curr_position[1]][curr_position[0]]
		curr_value = curr_position[2]

		options = []
		if curr_position[1]-1 >= 0:
			x,y = curr_position[0], curr_position[1]-1
			if heightmap[y][x]-height_value <= 1:
				options.append([x, y, heightmap[y][x]-height_value])
		if curr_position[1]+1 < len(heightmap):
			x,y = curr_position[0], curr_position[1]+1
			if heightmap[y][x]-height_value <= 1:
				options.append([x, y, heightmap[y][x]-height_value])
		if curr_position[0]-1 >= 0:
			x,y = curr_position[0]-1, curr_position[1]
			if heightmap[y][x]-height_value <= 1:
				options.append([x, y, heightmap[y][x]-height_value])
		if curr_position[0]+1 < len(heightmap[curr_position[1]]):
			x,y = curr_position[0]+1, curr_position[1]
			if heightmap[y][x]-height_value <= 1:
				options.append([x, y, heightmap[y][x]-height_value])

		for option in options:
			for item in queue:
				if item[0] == option[0] and item[1] == option[1]:
					new_effort = curr_value + heightmap[option[1]][option[0]]
					if new_effort < item[2]:
						item[2] = new_effort
						item[3] = [curr_position[0], curr_position[1]]
					break

		queue = update_queue(queue)

		visited.append(curr_position)

	path(end)
	paths.reverse()
	return len(paths)


with open('../inputs/input12') as f:
# with open('./test12') as f:
	heightmap = [[ord(x) for x in line.strip()] for line in f.readlines() if len(line) > 0]


	start = [0, 0, 0, None]
	end = [0, 0, sys.maxsize, None]
	for y in range(len(heightmap)):
		for x in range(len(heightmap[y])):
			if heightmap[y][x] == 83:
				start[0] = x
				start[1] = y
			elif heightmap[y][x] == 69:
				end[0] = x
				end[1] = y
	# print('Part 1:', dijkstra(start, end, heightmap))

	starts = []
	for y in range(len(heightmap)):
		for x in range(len(heightmap[y])):
			if heightmap[y][x] == ord('a'):
				starts.append([x,y,0,None])
	
	p = Pool(12)
	print('Part 2:', min([x for x in p.starmap(dijkstra, [(start, end, heightmap) for start in starts]) if x > 0]))
