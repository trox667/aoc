def play1(opponent, player):
	return {("A", "X"): 4, ("A", "Y"): 8, ("A", "Z"): 3,
			("B", "X"): 1, ("B", "Y"): 5, ("B", "Z"): 9,
			("C", "X"): 7, ("C", "Y"): 2, ("C", "Z"): 6}[(opponent, player)]

def play2(opponent, player):
	return {("A", "X"): 3, ("A", "Y"): 4, ("A", "Z"): 8,
			("B", "X"): 1, ("B", "Y"): 5, ("B", "Z"): 9,
			("C", "X"): 2, ("C", "Y"): 6, ("C", "Z"): 7}[(opponent, player)]

with open('../inputs/input2') as f:
	lines = f.readlines()
	part1 = 0
	part2 = 0
	for line in lines:
		opponent, player = line.strip().split(' ')
		part1 += play1(opponent,player)
		part2 += play2(opponent,player)
	print('Part 1:', part1)
	print('Part 2:', part2)
