import re

lines = [
    '""',
    '"abc"',
    '"aaa\\"aaa"',
    '"\\x27"'
]


# replace in the string
def handle_line(line: str):
    char_count = len(line)
    line = line.replace('\\\\', '1')
    line = line.replace('\\"', '2')
    p = re.compile('\\\\x([a-z]|[0-9]){2}')
    line = p.sub('3', line)
    count = len(line)
    return char_count, count - 2


# simple counting
def handle_line2(line: str):
    char_count = len(line)
    prev = None
    count = 0
    i = 0
    while i < len(line):
        c = line[i]
        if prev == '\\':
            if c == '"':
                count += 1
                i += 1
            elif c == 'x':
                count += 1
                i += 3
            prev = None
            continue
        if c == '\\':
            if line[i + 1] == '\\':
                i += 2
                count += 1
            else:
                prev = c
                i += 1
            continue
        if c != '"':
            count += 1

        i += 1

    return char_count, count


def part1(lines):
    total_char_count = 0
    total_count = 0
    for line in lines:
        char_count, count = handle_line2(line)
        print(line, char_count, count)
        total_char_count += char_count
        total_count += count

    print(total_char_count - total_count)


# replace in the string
def encode_line(line: str):
    original_count = len(line)
    line = line.replace('\\', '\\\\')
    line = '"' + line.replace('"', '\\"') + '"'

    return original_count, len(line)


def part2(lines):
    total_encoded_count = 0
    total_original_count = 0
    for line in lines:
        original_count, encoded_count = encode_line(line)
        total_encoded_count += encoded_count
        total_original_count += original_count
    print(total_encoded_count-total_original_count)



with open('inputs/input08') as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]
    # part1(lines)
    # part2(['""', '"abc"', '"aaa\\"aaa"', '"\\x27"'])
    part2(lines)