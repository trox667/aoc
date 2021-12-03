test = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

from collections import defaultdict


def load_file():
    with open('../inputs/input03') as file:
        return file.read()


def file_to_bits():
    return [line.strip() for line in load_file().splitlines() if line.strip()]
    # return test


def part1():
    bits_list = file_to_bits()
    bits_length = len(bits_list[0])
    result_one = defaultdict(int)
    result_zero = defaultdict(int)
    for bits in bits_list:
        for x in range(bits_length):
            if bits[x] == '1':
                result_one[x] += 1
            else:
                result_zero[x] += 1
    gamma, epsilon = '', ''
    for i in range(bits_length):
        if result_one[i] > result_zero[i]:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print(int(gamma, 2) * int(epsilon, 2))


def count_bits(index, bits_list):
    count_one = 0
    count_zero = 0
    for bits in bits_list:
        if bits[index] == '1':
            count_one += 1
        else:
            count_zero += 1
    return count_one, count_zero


def part2():
    bits_list = file_to_bits()
    bits_length = len(bits_list[0])

    oxygen_list = bits_list.copy()
    for x in range(bits_length):
        (a, b) = count_bits(x, oxygen_list)
        if a > b or a == b:
            oxygen_list = list(filter(lambda b: b[x] == '1', oxygen_list))
        else:
            oxygen_list = list(filter(lambda b: b[x] == '0', oxygen_list))
        if len(oxygen_list) == 1:
            break
    assert len(oxygen_list) == 1

    co2_scrubber_list = bits_list.copy()
    for x in range(bits_length):
        (a, b) = count_bits(x, co2_scrubber_list)
        if a > b or a == b:
            co2_scrubber_list = list(
                filter(lambda b: b[x] == '0', co2_scrubber_list))
        else:
            co2_scrubber_list = list(
                filter(lambda b: b[x] == '1', co2_scrubber_list))
        if len(co2_scrubber_list) == 1:
            break
    assert len(co2_scrubber_list) == 1

    print(int(oxygen_list[0], 2) * int(co2_scrubber_list[0], 2))


print(part1())
print(part2())
