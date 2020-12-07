import unittest
import re


class Bag:
    def __init__(self, name):
        self.name = name
        self.deps = {}

    def __repr__(self):
        return self.name + ' ' + str(self.deps)


def parse(line: str):
    multi_p = r'(?P<count>\d)?(?P<bag>([a-z]|\s)+) (bags|bag)'
    line = line.strip()
    first, rest = line.split(' contain ')
    first = re.sub(r'bags|bag', '', first)
    main_bag = Bag(first.strip())

    if 'no other' in rest:
        # no bag dep
        pass
    elif ',' in rest:
        # multi bag deps
        bags = rest.split(', ')
        for bag in bags:
            matches = re.search(multi_p, bag)
            count = int(matches.group('count'))
            bag = matches.group('bag').strip()
            main_bag.deps[bag] = count
    else:
        # single bag dep
        matches = re.search(multi_p, rest)
        count = int(matches.group('count'))
        bag = matches.group('bag').strip()
        main_bag.deps[bag] = count

    return main_bag


def part1():
    bags = [parse(line) for line in read_input()]
    queue = ['shiny gold']
    matching_bags = set()

    while len(queue) > 0:
        search_bag = queue.pop(0)
        for bag in bags:
            for dep in bag.deps:
                if search_bag == dep:
                    queue.append(bag.name)
                    matching_bags.add(bag.name)
    print(len(matching_bags))


def get_bag(name, bags):
    for bag in bags:
        if bag.name == name:
            return bag
    return None


def count_deps(bag, bags):
    if len(bag.deps) == 0:
        return 0
    else:
        count = 0
        for k, v in bag.deps.items():
            b = get_bag(k, bags)
            assert b
            count += v + v * count_deps(b, bags)
        return count


def part2():
    bags = [parse(line) for line in read_input()]
    shiny_bag = get_bag('shiny gold', bags)
    assert shiny_bag
    print(count_deps(shiny_bag, bags))


def read_input():
    with open('../inputs/input07') as input:
        return input.readlines()


if __name__ == '__main__':
    part1()
    part2()
