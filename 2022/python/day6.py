def run(line, step):
	for i in range(step, len(line), 1):
		unique_characters = set(line[i-step:i])
		if len(unique_characters) == step:
			return i
	return 0

with open('../inputs/input6') as f:
	lines = [line.strip() for line in f.readlines() if len(line) > 0]
	assert(len(lines) > 0)
	print('Part 1:', run(lines[0], 4))
	print('Part 2:', run(lines[0], 14))