with open('../inputs/input8') as f:
	input = f.readlines()
	forest = [[int(t) for t in line.strip()] for line in input if len(line) > 0]
	visible = [[False for _ in row] for row in forest]

	for y in range(len(forest)):
		max_left = -1
		max_right = -1
		for x in range(len(forest[y])):
			for xl in range(0, x):
				if forest[y][xl] > max_left:
					max_left = forest[y][xl]
					visible[y][xl] = True
			for xr in range(len(forest[y])-1, x, -1):
				if forest[y][xr] > max_right:
					max_right = forest[y][xr]
					visible[y][xr] = True

	for x in range(len(forest[0])):
		max_top= -1
		max_bottom = -1
		for y in range(len(forest)):
			for yu in range(0, y):
				if forest[yu][x] > max_top:
					max_top = forest[yu][x]
					visible[yu][x] = True
			for yb in range(len(forest)-1, y, -1):
				if forest[yb][x] > max_bottom:
					max_bottom = forest[yb][x]
					visible[yb][x] = True					

	print('Part 1:', sum([col for row in visible for col in row if col]))

	scenic_score = 0
	for y in range(len(forest)):
		for x in range(len(forest[y])):

			up, down, left, right = 0,0,0,0

			for yv in range(y-1, -1, -1):
				if forest[yv][x] < forest[y][x]:
					up+=1
				else:
					up+=1
					break
			for yv in range(y+1, len(forest)):
				if forest[yv][x] < forest[y][x]:
					down+=1
				else:
					down+=1
					break
			for xh in range(x-1, -1, -1):
				if forest[y][xh] < forest[y][x]:
					left+=1
				else:
					left+=1
					break
			for xh in range(x+1, len(forest[y])):
				if forest[y][xh] < forest[y][x]:
					right+=1
				else:
					right+=1
					break
			scenic_score = max(scenic_score, up * down * left * right)

	print('Part 2:', scenic_score)