from collections import defaultdict


def get_games():
    with open('../input/input02') as f:
        lines = [line.strip() for line in f.readlines() if len(line) > 0]
        games = {}
        for line in lines:
            game_id = int(line.split(':')[0].replace("Game ", ""))
            sets = [set.strip() for set in line.split(':')[1].split('; ')]
            sets = [set.split(', ') for set in sets]
            game_sets = []
            for set in sets:
                game_set = defaultdict(int, letters=['red', 'green', 'blue'])
                for entry in set:
                    count = int(entry.split(' ')[0])
                    color = entry.split(' ')[1]
                    game_set[color] = count
                game_sets.append(game_set)
            games[game_id] = game_sets
        return games


def is_game_valid(game_sets):
    for game_set in game_sets:
        if game_set['red'] > 12 or game_set['green'] > 13 or game_set['blue'] > 14:
            return False
    return True


def part1():
    print(sum([game_id for game_id, game_sets in get_games().items()
          if is_game_valid(game_sets)]))


def power_game(game_sets):
    red, green, blue = 0, 0, 0
    for game_set in game_sets:
        red = max(red, game_set['red'])
        green = max(green, game_set['green'])
        blue = max(blue, game_set['blue'])
    return red * green * blue


def part2():
    print(sum([power_game(game_sets) for _, game_sets in get_games().items()]))


if __name__ == '__main__':
    part1()
    part2()
