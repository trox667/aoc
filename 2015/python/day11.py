end = ord('z')
begin = ord('a')


def increment(word, index):
    if index < 0:
        return word

    last = ord(word[index])
    if last == end:
        word = word[0:index] + chr(begin) + word[index + 1:]
        word = increment(word, index - 1)
    else:
        word = word[0:index] + chr(last + 1) + word[index + 1:]
    return word


def increasing_straight(word):
    if len(word) < 3:
        return False

    for i in range(2, len(word)):
        tmp = [ord(c) for c in word[i - 2:i + 1]]
        if tmp[0] + 2 == tmp[1] + 1 == tmp[2]:
            return True

    return False


def not_contain_iol(word):
    return not any(c in word for c in 'iol')


def two_pairs(word):
    count = 0
    chars = set(word)
    for c in chars:
        if word.count(c + c) == 1:
            count += 1
    return count >= 2


def validate(word):
    return not_contain_iol(word) and two_pairs(word) and increasing_straight(
        word)


def part1():
    with open('inputs/input11') as file:
        input = file.read().strip()
        word = increment(input, len(input) - 1)
        while not validate(word):
            word = increment(word, len(word) - 1)

        print(word)


def part2():
    with open('inputs/input11') as file:
        input = file.read().strip()
        word = increment(input, len(input) - 1)
        while not validate(word):
            word = increment(word, len(word) - 1)

        word = increment(word, len(input) - 1)
        while not validate(word):
            word = increment(word, len(word) - 1)

        print(word)


part1()
part2()
