with open('../inputs/input6') as f:
	lines = [line.strip() for line in f.readlines() if len(line) > 0]

	assert(len(lines) > 0)
	line = lines[0]

	part1 = 0
	for i in range(4, len(line), 1):
		unique_characters = set(line[i-4:i])
		if len(unique_characters) == 4:
			part1 = i
			print("Part 1:", part1)
			break
	part2 = 0
	for i in range(14, len(line), 1):
		unique_characters = set(line[i-14:i])
		if len(unique_characters) == 14:
			part2 = i
			print("Part 2:", part2)
			break