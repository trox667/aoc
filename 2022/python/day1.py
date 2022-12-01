with open('../inputs/input1') as f:
	groups = f.read().split('\n\n')
	sums = []
	for group in groups:
		sums.append(sum([int(x) for x in group.split('\n') if len(x) > 0]))
	sums.sort(reverse=True)
	print(sums[0])

	print(sum(sums[0:3]))
	
