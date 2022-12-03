with open('../inputs/input3') as f:
	lines = [line.strip() for line in f.readlines() if len(line) > 0]
	part1 = 0
	for line in lines:
		first = line[:len(line)//2]
		second = line[len(line)//2:]
		for token in first:
			if token in second:
				if token.islower():
					part1 += ord(token) - 96
				else:
					part1 += ord(token) - 38
				break
	print('Part 1:', part1)

	part2 = 0
	for i in range(0, len(lines), 3):
		first = lines[i]
		second = lines[i+1]
		third = lines[i+2]
		for token in first:
			if token in second and token in third:
				if token.islower():
					part2 += ord(token) - 96
				else:
					part2 += ord(token) - 38
				break
	print('Part 2:', part2)
