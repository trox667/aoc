with open('../inputs/input4') as f:
	lines = f.readlines()
	part1 = 0
	part2 = 0

	for line in lines:
		items = []
		for tokens in line.strip().split(','):
			item = [int(token) for token in tokens.split('-')]
			items.append(item)
		range1 = set(range(items[0][0], items[0][1]+1))
		range2 = set(range(items[1][0], items[1][1]+1))
		if range1.issubset(range2) or range2.issubset(range1):
			part1 += 1
		if range1.intersection(range2):
			part2+= 1

	print('Part 1:', part1)
	print('Part 2:', part2)	