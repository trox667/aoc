import unittest
import re
import collections


def parse_class(line):
    pattern = r"^(?P<name>.+): (?P<n1>\d+)-(?P<n2>\d+) or (?P<n3>\d+)-(?P<n4>\d+)$"
    matches = re.search(pattern, line)
    name = matches.group('name')
    n1 = matches.group('n1')
    n2 = matches.group('n2')
    n3 = matches.group('n3')
    n4 = matches.group('n4')
    return (name, int(n1), int(n2), int(n3), int(n4))


def parse(lines):
    rules = dict()
    ticket = list()
    nearby_tickets = list()
    state = ''

    for line in lines:
        if state == 'your':
            ticket = [int(t) for t in line.strip().split(',')]
            state = ''
        elif state == 'nearby':
            nearby_tickets.append([int(t) for t in line.strip().split(',')])
        if 'or' in line:
            (name, n1, n2, n3, n4) = parse_class(line)
            rules[name] = [n1, n2, n3, n4]
        elif 'your' in line:
            state = 'your'
        elif 'nearby' in line:
            state = 'nearby'
    return (rules, ticket, nearby_tickets)


def check_rule(value, rule):
    [n1, n2, n3, n4] = rule
    return n1 <= value <= n2 or n3 <= value <= n4


def check_rules(values, rules):
    nums = []
    for value in values:
        rule_res = []
        for (name, rule) in rules.items():
            rule_res.append(check_rule(value, rule))
        if not any(rule_res):
            nums.append(value)
    return nums


def run(lines):
    (rules, ticket, nearby_tickets) = parse(lines)
    nums = []
    for values in nearby_tickets:
        nums += check_rules(values, rules)

    return sum(nums)


def part1():
    print(run(read_input()))


def rules_dict(values, rules):
    R = dict()
    for (name, rule) in rules.items():
        res = []
        for value in values:
            res.append(check_rule(value, rule))
        R[name] = res
    return R


def run2(lines):
    (rules, ticket, nearby_tickets) = parse(lines)
    valid_tickets = []
    # filter valid tickets
    for values in nearby_tickets:
        if len(check_rules(values, rules)) == 0:
            valid_tickets.append(values)

    # store the length of a ticket (all should have same length)
    values_len = len(valid_tickets[0])

    # create a dictionary with matches for each value
    # values: 3 9 18
    # class: 0-1 or 4-19
    # row 0-5 or 8-19
    # seat 0-13 or 16-19
    # ->
    # false true true <- class
    # true true true <- row
    # true false true <- seat
    matches = []
    for values in valid_tickets:
        matches.append(rules_dict(values, rules))

    # create a list with possible result options
    # [1] <- class
    # [1,2,3] <- row
    # [1,3] <- seat
    options = collections.defaultdict(list)
    for (name, _) in rules.items():
        # search in all ticket values (columns)
        for i in range(0, values_len):
            L = []
            # search through all matches (rows)
            for match in matches:
                L.append(match[name][i])
            # if all rows for this column are true
            # add it as an option
            if all(L):
                options[name].append(i)

    # loop until the option dict is empty
    R = dict()
    while 1:
        take = -1
        rem = ''
        for (option, values) in options.items():
            # the option has only one solution
            if len(values) == 1:
                take = values[0]
                R[take] = option
            # the option should be removed
            elif len(values) == 0:
                rem = option

        # an option 'rem' should be removed
        if rem != '':
            options.pop(rem)
            rem = ''
        # remove the value 'take' from all options
        for (option, values) in options.items():
            if take >= 0 and take in values:
                values.remove(take)
        # reset take after removal
        take = -1

        # break loop check
        if len(options) == 0:
            break

    r = 1
    for (i, name) in R.items():
        if name.startswith('departure'):
            r *= ticket[i]

    print(r)


def part2():
    run2(read_input())
    pass


def read_input():
    with open('../inputs/input16') as input:
        return [line for line in input if not line.isspace()]


test_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

test_input2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


class TestPart1(unittest.TestCase):
    def test_parse_class(self):
        parse_class(test_input.split('\n')[0])
        parse_class(test_input.split('\n')[1])
        parse_class(test_input.split('\n')[2])

    def test_parse(self):
        parse([line for line in test_input.split('\n') if not line.isspace()])

    def test_rule(self):
        rules = {'class': [1, 3, 5, 7], 'row': [
            6, 11, 33, 44], 'seat': [13, 40, 45, 50]}
        self.assertEqual(check_rules([7, 1, 14], rules), [])
        self.assertEqual(check_rules([7, 3, 47], rules), [])
        self.assertEqual(check_rules([40, 4, 50], rules), [4])
        self.assertEqual(check_rules([55, 2, 20], rules), [55])
        self.assertEqual(check_rules([38, 6, 12], rules), [12])

    def test_run(self):
        self.assertEqual(
            run([line for line in test_input.split('\n') if not line.isspace()]), 71)


class TestPart2(unittest.TestCase):
    def test_run2(self):
        run2([line for line in test_input2.split('\n') if not line.isspace()])


if __name__ == '__main__':
    part1()
    part2()
    # unittest.main()
