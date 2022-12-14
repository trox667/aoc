sand_origin = 500, 0


def draw_sample(rock_paths, sand):
    min_x = 490
    max_x = 520
    min_y = 0
    max_y = 12

    for y in range(min_y, max_y):
        row = []
        for x in range(min_x, max_x):
            if (x, y) in sand:
                row.append('o')
            elif (x, y) in rock_paths:
                row.append('#')
            else:
                row.append('.')
        print("".join(row))


# with open('test14') as f:
with open('../inputs/input14') as f:
    lines = [line.strip() for line in f.readlines() if len(line) > 0]

    rock_paths = set()
    for line in lines:
        tokens = line.split(' -> ')
        xp, yp = None, None
        for token in tokens:
            x, y = map(int, token.split(','))
            if xp == yp == None:
                xp, yp = x, y
            else:
                if xp == x:
                    for yc in range(yp, y - 1 if yp > y else y + 1, -1 if yp > y else 1):
                        rock_paths.add((x, yc))
                elif yp == y:
                    for xc in range(xp, x - 1 if xp > x else x + 1, -1 if xp > x else 1):
                        rock_paths.add((xc, y))
                xp, yp = x, y

    sand = set()
    max_y = max([y for _, y in rock_paths])
    prev_sand_count = 0

    # for i in range(30):
    while 1:
        x, y = sand_origin

        while y < max_y:
            if (x, y + 1) in rock_paths or (x, y + 1) in sand:
                if (x - 1, y + 1) not in rock_paths and (x - 1, y + 1) not in sand:
                    x -= 1
                    y += 1
                elif (x + 1, y + 1) not in rock_paths and (x + 1, y + 1) not in sand:
                    x += 1
                    y += 1
                else:
                    break
            else:
                y += 1
        if y < max_y:
            sand.add((x, y))
        if len(sand) > prev_sand_count:
            prev_sand_count = len(sand)
        else:
            break

    print(len(sand))
    # draw_sample(rock_paths, sand)

    # part2
    sand = set()
    max_y += 2
    prev_sand_count = 0

    while sand_origin not in sand:
        x, y = sand_origin

        while y < max_y:
            if (x, y + 1) in rock_paths or (x, y + 1) in sand or y + 1 >= max_y:
                if (x - 1, y + 1) not in rock_paths and (x - 1, y + 1) not in sand and y + 1 < max_y:
                    x -= 1
                    y += 1
                elif (x + 1, y + 1) not in rock_paths and (x + 1, y + 1) not in sand and y + 1 < max_y:
                    x += 1
                    y += 1
                else:
                    break
            else:
                y += 1
        if y < max_y:
            sand.add((x, y))
        if len(sand) > prev_sand_count:
            prev_sand_count = len(sand)
        else:
            break

    print(len(sand))
    # draw_sample(rock_paths, sand)
