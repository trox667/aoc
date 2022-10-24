# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
import re


def read_line(line: str):
    p = re.compile('(-?\\d+)')
    matches = p.findall(line)
    return [int(match) for match in matches]


def ingredients(lines):
    return [read_line(line) for line in lines]


def part1():
    with open('inputs/input15') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        ing = ingredients(lines)
        max_score = 0
        for i0 in range(1, 101):
            for i1 in range(1, 101 - i0):
                for i2 in range(1, 101 - i0 - i1):
                    score = 1
                    i3 = 100 - i0 - i1 - i2
                    for i in range(len(ing[0]) - 1):
                        score *= max(i0 * ing[0][i] + i1 * ing[1][i] + i2 * ing[2][i] + i3 * ing[3][i], 0)
                    if score > max_score:
                        max_score = score

        print(max_score)


part1()
