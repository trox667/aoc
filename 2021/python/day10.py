def load_file():
    with open('../inputs/input10') as file:
        return file.read()


test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

POINTS_PT1 = {'E': 0, ')': 3, '}': 1197, ']': 57, '>': 25137}
POINTS_PT2 = {'E': 0, ')': 1, '}': 3, ']': 2, '>': 4}
OPEN_CLOSING = {'(': ')', '{': '}', '[': ']', '<': '>'}
CLOSING_OPEN = {')': '(', '}': '{', ']': '[', '>': '<'}


def get_chunks():
    # data = test
    data = load_file()
    return [line for line in data.splitlines()]


def parse(chunk, return_on_error=True):
    """Parse a given chunk and return a tuple with a wrong symbol or 'E' and a list of missing symbols"""
    stack = [chunk[0]]
    i = 1
    error = False
    for c in chunk[1:]:
        if c in OPEN_CLOSING.keys():
            stack.append(c)
        if c in CLOSING_OPEN.keys():
            if len(stack) > 0 and CLOSING_OPEN[c] == stack[len(stack) - 1]:
                stack.pop()
            else:
                error = True
        if error and return_on_error:
            return chunk[i], []
        i += 1

    if not error:
        stack.reverse()
        return 'E', [OPEN_CLOSING[c] for c in stack]
    else:
        return 'E', []


def part1():
    return sum(map(lambda t: POINTS_PT1[t[0]],
                   [parse(chunk) for chunk in get_chunks()]))


def part2():
    results = []
    for added in map(lambda t: t[1], [parse(chunk) for chunk in get_chunks()]):
        points = 0
        for a in added:
            points *= 5
            points += POINTS_PT2[a]
        if points > 0:
            results.append(points)
    results.sort()
    return results[len(results) // 2]


print(part1())  # 26397
print(part2())  # 288957
