from collections import defaultdict

with open('../input/input04') as f:
    lines = [line.strip() for line in f.readlines() if len(line) > 0]
    score = 0
    for line in lines:
        tokens = line.split('|')
        winning = set([int(t) for t in tokens[0].split(':')[1].split()])
        own = set([int(t) for t in tokens[1].split()])
        matches = list(winning & own)
        if (len(matches) > 0):
            score += 2 ** (len(matches)-1)
    print(score)


with open('../input/input04') as f:
    lines = [line.strip() for line in f.readlines() if len(line) > 0]
    cards = defaultdict(int)
    new_cards = defaultdict(int)
    idx = 1
    for line in lines:
        tokens = line.split('|')
        winning = set([int(t) for t in tokens[0].split(':')[1].split()])
        own = set([int(t) for t in tokens[1].split()])
        matches = list(winning & own)
        cards[idx] = len(matches)
        idx += 1
    for curr_card in range(1, idx):
        new_cards[curr_card] = 1

    for curr_card in range(1, idx):
        for i in range(new_cards[curr_card]):
            matches = cards[curr_card]
            for j in range(curr_card+1, curr_card+matches+1):
                new_cards[j] += 1

    print(sum(new_cards.values()))
