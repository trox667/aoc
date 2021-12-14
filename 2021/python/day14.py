import sys
from collections import defaultdict


def load_file():
    with open('../inputs/input14') as file:
        return file.read()


def get_start_rules():
    data = load_file()
    start = data.splitlines()[0]
    rules = {}
    for rule in data.splitlines()[2:]:
        pair_rule = rule.split(' -> ')
        rules[pair_rule[0]] = [pair_rule[0][0] + pair_rule[1],
                               pair_rule[1] + pair_rule[0][1]]
    return start, rules


def init(polymer):
    pairs_counter = defaultdict(int)
    for pair in [a + b for a, b in zip(polymer[:-1], polymer[1:])]:
        pairs_counter[pair] += 1
    return pairs_counter


def next(pairs_counter, rules):
    new_pairs_counter = defaultdict(int)
    for pair, count in pairs_counter.items():
        for combination in rules.get(pair):
            new_pairs_counter[combination] += count
    return new_pairs_counter


def count(pairs_counter, last_element):
    element_counter = defaultdict(int)
    for pair, count in pairs_counter.items():
        element_counter[pair[0]] += count
    element_counter[last_element[-1]] += 1

    min_count, max_count = sys.maxsize, 0
    for element, count in element_counter.items():
        if count < min_count:
            min_count = count
        elif count > max_count:
            max_count = count
    return max_count - min_count


def run(steps):
    polymer, rules = get_start_rules()
    pairs_counter = init(polymer)
    for _ in range(steps):
        pairs_counter = next(pairs_counter, rules)
    return count(pairs_counter, polymer[-1])


def part1():
    return run(10)


def part2():
    return run(40)


print(part1())
print(part2())
