import unittest


def get_lwh(lwh):

    lwh = [int(i) for i in lwh.split('x')]
    if len(lwh) < 3:
        return 0
    else:
        l, w, h = lwh
        return (l, w, h)


def surface(lwh):
    l, w, h = get_lwh(lwh)
    a = l * w
    b = w * h
    c = h * l
    d = min(a, b, c)
    return 2 * a + 2 * b + 2 * c + d


def part1():
    with open('input02') as input:
        print(sum([surface(lwh) for lwh in input]))


def volume(lwh):
    l, w, h = get_lwh(lwh)
    return l * w * h


def smallest_perimeter(lwh):
    l, w, h = get_lwh(lwh)
    a = l+w
    b = w+h
    c = h+l
    return 2 * min(a, b, c)


def ribbon(lwh):
    return smallest_perimeter(lwh) + volume(lwh)


def part2():
    with open('input02') as input:
        print(sum([ribbon(lwh) for lwh in input]))


class Part1(unittest.TestCase):
    def test_surface(self):
        self.assertEqual(surface('2x3x4'), 58)
        self.assertEqual(surface('1x1x10'), 43)


class Part2(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(volume('2x3x4'), 24)
        self.assertEqual(volume('1x1x10'), 10)

    def test_shortest_distance(self):
        self.assertEqual(smallest_perimeter('2x3x4'), 10)
        self.assertEqual(smallest_perimeter('1x1x10'), 4)

    def test_ribbon(self):
        self.assertEqual(ribbon('2x3x4'), 34)
        self.assertEqual(ribbon('1x1x10'), 14)


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
