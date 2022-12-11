from copy import deepcopy
from math import lcm

def to_op(input):
	return lambda x: eval(input, {}, {"old": x})

def run(monkeys, steps, part2=False):
	monkeys = deepcopy(monkeys)
	divs = []
	for i in monkeys:
		divs.append(monkeys[i][2])
	modulus = lcm(*divs)
	for _ in range(steps):
		for i in monkeys:
			monkey = monkeys[i]
			for item in monkey[0]:
				monkey[4] = monkey[4]+1
				if part2:
					worrylevel = monkey[1](item) % modulus
				else:
					worrylevel = monkey[1](item) // 3
				if worrylevel % monkey[2] == 0:
					monkeys[monkey[3][0]][0].append(worrylevel)
				else:
					monkeys[monkey[3][1]][0].append(worrylevel)

			monkey[0] = []

	top_two = sorted(monkeys.items(), key=lambda item: item[1][4], reverse=True)[0:2]
	print(top_two[0][1][4] * top_two[1][1][4])

with open('../inputs/input11') as f:
	monkey_dict = {}
	monkeys = f.read().split('\n\n')
	for monkey in monkeys:
		entries = monkey.split('\n')
		i = int(entries[0].split(' ')[1].replace(':', ''))
		items = [int(t) for t in entries[1].split(': ')[1].split(', ')]
		op = to_op(entries[2].split(' = ')[1])
		test = int(entries[3].split(' by ')[1])
		test_true = int(entries[4].split('monkey ')[1])
		test_false = int(entries[5].split('monkey ')[1])
		monkey_dict[i]  = [items, op, test, [test_true, test_false], 0]
	run(monkey_dict, 20)
	run(monkey_dict, 10000, True)