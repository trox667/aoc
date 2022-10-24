from collections import defaultdict
from itertools import permutations


def test_input():
    return '''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.'''


def parse_line(line: str):
    line = line.strip('.')
    tokens = line.split(' ')
    name = tokens[0]
    action = tokens[2]
    score = int(tokens[3])
    neighbor = tokens[-1]
    if action == 'lose':
        score = -score

    return name, score, neighbor


def create_attendees_dict(lines):
    attendees = set()
    score_dict = defaultdict(lambda: {})
    for line in lines:
        name, score, neighbor = parse_line(line)
        attendees.add(name)
        score_dict[name][neighbor] = score

    return attendees, score_dict


def is_ok(seating, score_dict):
    score = 0
    for i in range(0, len(seating)):
        name = seating[i]
        neighbor_left = seating[i - 1]
        neighbor_right = seating[0] if i + 1 > len(seating) - 1 else seating[
            i + 1]
        score_left = score_dict[name][neighbor_left]
        score_right = score_dict[name][neighbor_right]
        if score_left + score_right < 0:
            return False, 0
        score += score_left + score_right
    return True, score


def loop(attendees, score_dict):
    max_score = 0
    last = attendees.pop()
    for p in permutations(attendees):
        seating = list(p) + [last]
        ok, score = is_ok(seating, score_dict)
        if score > max_score:
            max_score = score
        # print(ok, score, seating)
    return max_score


def add_user(attendees, score_dict):
    for attendee in attendees:
        score_dict[attendee]['Me'] = 0
        score_dict['Me'][attendee] = 0
    attendees.add('Me')


def part1():
    with open('inputs/input13') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        attendees, score_dict = create_attendees_dict(lines)
        print(loop(attendees, score_dict))


def part2():
    with open('inputs/input13') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        attendees, score_dict = create_attendees_dict(lines)
        add_user(attendees, score_dict)
        print(loop(attendees, score_dict))


# Test

def test():
    lines = test_input().splitlines()
    attendees, score_dict = create_attendees_dict(lines)
    # is_ok(('David', 'Alice', 'Bob', 'Carol'), score_dict)
    loop(attendees, score_dict)


# test()
# part1()
part2()