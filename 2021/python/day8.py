from collections import Counter

UNIQUE_DIGIT_SEGMENT = {2, 3, 4, 7}
DIGITS = {'0': [0, 1, 2, 4, 5, 6],
          '1': [2, 5],
          '2': [0, 2, 3, 4, 6],
          '3': [0, 2, 3, 5, 6],
          '4': [1, 2, 3, 5],
          '5': [0, 1, 3, 5, 6],
          '6': [0, 1, 3, 4, 5, 6],
          '7': [0, 2, 5],
          '8': [0, 1, 2, 3, 4, 5, 6],
          '9': [0, 1, 2, 3, 5, 6]}


def load_file():
    with open('../inputs/input08') as file:
        return file.read()


def create_input():
    line_tokens = [line.strip().split('|') for line in load_file().splitlines()
                   if
                   line.strip()]
    return [(line[0].strip().split(), line[1].strip().split()) for line in
            line_tokens]


def update_segments(idx, word, segments):
    for c in word:
        if c not in segments:
            segments[idx] = c
            return


def determine_digit(words):
    words.sort(key=len)
    segments = [None, None, None, None, None, None, None]
    rest = []
    for word in words:
        if len(word) == 2:
            segments[2] = word[0]
            segments[5] = word[1]
        elif len(word) == 3:
            update_segments(0, word, segments)
        elif len(word) == 4:
            update_segments(1, word, segments)
            update_segments(3, word, segments)
        elif len(word) == 7:
            update_segments(4, word, segments)
            update_segments(6, word, segments)
        else:
            rest.append(word)

    lf = Counter(''.join(filter(lambda w: len(w) == 5, rest)))
    ls = Counter(''.join(filter(lambda w: len(w) == 6, rest)))

    if lf[segments[1]] != 1:
        segments[1], segments[3] = segments[3], segments[1]

    if ls[segments[2]] != 2:
        segments[2], segments[5] = segments[5], segments[2]

    if ls[segments[4]] != 2:
        segments[4], segments[6] = segments[6], segments[4]

    return segments


def digit_from_segment(word, segment):
    for number, digit_segments in DIGITS.items():
        if len(digit_segments) != len(word):
            continue
        if Counter(word) == Counter(
                ''.join([segment[digit_segment] for digit_segment in
                         digit_segments])):
            return number

    raise Exception('Could not find digit')


def part1():
    return sum([len(word) in UNIQUE_DIGIT_SEGMENT for line in
                create_input() for
                word in
                line[1]])


def part2():
    result = 0
    lines = create_input()
    for line in lines:
        segments = determine_digit(line[0])
        result += int(''.join([digit_from_segment(word, segments)
                          for word in line[1]]))
    return result


print(part1())  # 318
print(part2())  # 996280
