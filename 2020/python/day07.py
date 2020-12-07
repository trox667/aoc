import unittest


class Bag:
    def __init__(self, name, count=1, deps=dict(), deps_count=dict()):
        self.name = name
        self.count = count
        self.deps = deps
        self.deps_count = deps_count

    def __repr__(self):
        return '' + str(self.count) + ' ' + self.name + str(self.deps)


def parse(line: str):
    line = line.strip()
    if ',' in line:
        bag, tail = line.split(' contain ')
        bag = bag.replace(' bags', '')
        bag = bag.replace(' bag', '')
        deps = tail.split(', ')
        dep_bags = dict()
        deps_count = dict()
        for d in deps:
            count = d[:1]
            text = d[2:]
            text = text.replace(' bags', '')
            text = text.replace(' bag', '')
            text = text.replace('.', '')
            dep_bags[text] = Bag(text, int(count))
            deps_count[text] = int(count)
        return Bag(bag, 1, dep_bags, deps_count)
    elif 'no other' in line:
        bag = line[0:line.find(' contain')]
        bag = bag.replace(' bags', '')
        bag = bag.replace(' bag', '')
        return Bag(bag)
    else:
        bag, tail = line.split(' contain ')
        bag = bag.replace(' bags', '')
        bag = bag.replace(' bag', '')
        count = tail[:1]
        text = tail[2:]
        text = text.replace(' bags', '')
        text = text.replace(' bag', '')
        text = text.replace('.', '')
        dep_bags = dict()
        dep_count = dict()
        dep_bags[text] = Bag(text, int(count))
        dep_count[text] = int(count)
        return Bag(bag, 1, dep_bags, dep_count)


# create a dict of bags
# find all bags having shiny gold as dep
# loop over all found bags having the prev found one as dep
# continue until no bags found


def run(bags):
    search = ['shiny gold']
    collected_bags = set()
    while len(search) > 0:
        s = search[0]
        for bag in bags:
            if bag.name in collected_bags:
                continue
            for d in bag.deps:
                if s == d:
                    search.append(bag.name)
                    collected_bags.add(bag.name)
        search.remove(s)
    print(collected_bags)
    return len(collected_bags)


def part1():
    bags = [parse(line) for line in read_input()]
    print(run(bags))


def find_bag(name, bags):
    for bag in bags:
        if bag.name == name:
            return bag


def count_deps(bag, bags):
    if len(bag.deps) == 0:
        return 0
    else:
        count = 0
        for d in bag.deps:
            b = find_bag(d, bags)
            c = bag.deps_count[d]
            count += c
            if b != None:
                count += c * count_deps(b, bags)
        return count


def run2(bags):
    shiny_bag = find_bag('shiny gold', bags)
    count = 0
    # for _, c in shiny_bag.deps_count.items():
    #     count += c
    count += count_deps(shiny_bag, bags)
    return count


def part2():
    bags = [parse(line) for line in read_input()]
    print(run2(bags))


def read_input():
    with open('../inputs/input07') as input:
        return input.readlines()


test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test_input2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


class TestPart1(unittest.TestCase):
    pass

    # def test_parse(self):
    #     lines = test_input.split('\n')
    #     for line in lines:
    #         print(parse(line))

    def test_run(self):
        pass
        # lines = test_input.split('\n')
        # bags = [parse(line) for line in lines]
        # run(bags)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        lines = test_input2.split('\n')
        bags = [parse(line) for line in lines]
        print(run2(bags))


if __name__ == '__main__':
    # part1()
    part2()
    # unittest.main()
    pass
