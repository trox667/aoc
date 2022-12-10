WIDTH = 40
HEIGHT = 6

def draw(pixels):
	for y in range(HEIGHT):
		for x in range(WIDTH):
			print(pixels[y * WIDTH + x], end='')
		print()

with open('../inputs/input10') as f:
	lines = [line.strip() for line in f.readlines() if len(line) > 0]
	ops =  []
	for line in lines:
		if line.startswith('addx'):
			ops.append(None)
			ops.append(int(line.split(' ')[1]))
		else:
			ops.append(None)
	signal_strengths = 0
	register_x = 1
	cycle = 0
	pixels = ['.' for _ in range(WIDTH * HEIGHT)]
	for op in ops:
		if register_x in {cycle % 40, (cycle + 1) % 40, (cycle - 1) % 40}:
			pixels[cycle] = '#'
		cycle += 1
		if cycle in {20, 60, 100, 140, 180, 220}:
			signal_strengths += cycle * register_x
		if op != None:
			register_x += op

	print('Part 1: ', signal_strengths)
	print('Part 2:')
	draw(pixels)