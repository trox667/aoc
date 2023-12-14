# read input
lines = [line for line in open('../input/input13').read().splitlines()]
groups = []
group = []
for line in lines:
    if len(line) == 0:
        groups.append(group)
        group = []
    else:
        group.append(line)
groups.append(group)


def print_groups():
    for group in groups:
        for line in group:
            print(line)
        print()


def is_horizontal_equal(line1, line2):
    return line1 == line2


def check_horizontal(group, y1, y2):
    if y1 < 0 or y2 > len(group)-1:
        return 0

    result = 0
    if is_horizontal_equal(group[y1], group[y2]):
        result = 1
        result += check_horizontal(group, y1-1, y2+1)
    return result


def is_vertical_equal(column1, column2, group):
    for line in group:
        if line[column1] != line[column2]:
            return False
    return True


def check_vertical(group, x1, x2):
    if x1 < 0 or x2 > len(group[0])-1:
        return 0

    result = 0
    if is_vertical_equal(x1, x2, group):
        result = 1
        result += check_vertical(group, x1-1, x2+1)
    return result


def vertical(group):
    for x in range(0, len(group[0])-1):
        result = check_vertical(group, x, x+1)
        requiredLen = min(x+1, len(group[0]) - (x+1))
        if result >= requiredLen:
            print("x", x+1, result, requiredLen)
            return x+1
    return 0


def horizontal(group):
    for y in range(0, len(group)-1):
        result = check_horizontal(group, y, y+1)
        requiredLen = min(y+1, len(group) - (y+1))
        if result >= requiredLen:
            print("y", y+1, result, requiredLen)
            return y+1
    return 0

total = 0
for group in groups:
    h = horizontal(group)
    v = vertical(group)
    total += v + h * 100
print(total)
