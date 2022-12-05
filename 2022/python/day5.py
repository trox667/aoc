from itertools import takewhile
from copy import deepcopy

with open('../inputs/input5') as f:
	lines = f.readlines()
	crates_count = len(lines[0]) // 4

	stacks = [[] for _ in range(crates_count)]
	
	crate_lines = list(takewhile(lambda line: line != '\n', lines))[:-1]
	for crate_line in crate_lines:
		for i in range(crates_count):
			token = crate_line[i*4:(i+1)*4]
			if token[0] == '[':
				stacks[i].insert(0, token[1])

	stacks2 = deepcopy(stacks)			
	instruction_lines = [line.strip() for line in lines if line.startswith('move')]				
	for instruction in instruction_lines:
		_, m, _, f, _, t = instruction.split(' ')
		idx = len(stacks[int(t)-1])
		for i in range(int(m)):
			stacks[int(t)-1].append(stacks[int(f)-1].pop())

			stacks2[int(t)-1].insert(idx, stacks2[int(f)-1].pop())

	for stack in stacks:
		print(stack[-1], end='')
	print()
	for stack in stacks2:
		print(stack[-1], end='')
	print()