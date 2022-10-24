import json
import re


def part1():
    with open('inputs/input12') as file:
        i = file.read()
        p = re.compile('(-?[0-9]+)')
        matches = re.findall(p, i)
        print(sum([int(match) for match in matches]))


def is_number(n):
    return isinstance(n, (int, float)) and not isinstance(n, bool)


def traverse(o):
    result = 0
    if is_number(o):
        result += o
    elif isinstance(o, list):
        for item in o:
            result += traverse(item)
    elif isinstance(o, dict):
        if 'red' not in o.values():
            for item in o.values():
                result += traverse(item)
    return result


def part2():
    with open('inputs/input12') as file:
        i = file.read()
        o = json.loads(i)
        print(traverse(o))


part2()
