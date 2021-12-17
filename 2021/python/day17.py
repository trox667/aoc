import re

test = "target area: x=20..30, y=-10..-5"


def load_file():
    with open('../inputs/input17') as file:
        return file.read()


def get_input():
    data = load_file()
    # data = test
    line = data.splitlines()[0]
    x, y = line.split(': ')[1].split(', ')
    xs, xe = re.findall('(-?\\d+)..(-?\\d+)', x)[0]
    ys, ye = re.findall('(-?\\d+)..(-?\\d+)', y)[0]
    return range(int(xs), int(xe) + 1), range(int(ys), int(ye) + 1)


def hit2(x, y, sx, sy, ex, ey):
    return sx <= x <= ex and sy >= y >= ey


def shoot(ix, iy, sx, sy, ex, ey):
    step = 0
    x, y = 0, 0
    vx, vy = ix, iy
    max_y = 0
    while x <= ex and y >= ey:
        # print(f'step {step} -> x,y ({x},{y}) - vx,vy ({vx},{vy})')
        x += vx
        y += vy
        if y > max_y:
            max_y = y
        if hit2(x, y, sx, sy, ex, ey):
            return max_y
        if vx > 0:
            vx -= 1
        vy -= 1
        step += 1
    return None


def part1():
    range_x, range_y = get_input()
    hits = []
    sx, sy = min(range_x), max(range_y)
    ex, ey = max(range_x), min(range_y)
    for x in range(1, ex + 1):
        for y in range(ey, 1000):
            # print(f'shoot ({x},{y})')
            max_y = shoot(x, y, sx, sy, ex, ey)
            if max_y is not None:
                hits.append((x, y, max_y))

    # hit = shoot(7, 2, max(range_x), min(range_y), target)
    print(max(hits, key=lambda t: t[2]))
    print(len(hits))
    # print(hits)


def part2():
    pass


print(part1())
print(part2())
