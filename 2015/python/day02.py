import unittest


def surface(lwh):
    lwh = [int(i) for i in lwh.split('x')]
    if len(lwh) < 3:
        return 0
    else:
        l, w, h = lwh
        a = l * w
        b = w * h
        c = h * l
        d = min(a, min(b, c))
        return 2 * a + 2 * b + 2 * c + d


def part1():
    with open('input02') as input:
        print(sum([surface(lwh) for lwh in input]))


class Part1(unittest.TestCase):
    def test_surface(self):
        self.assertEqual(surface('2x3x4'), 58)
        self.assertEqual(surface('1x1x10'), 43)


if __name__ == '__main__':
    part1()
    unittest.main()
