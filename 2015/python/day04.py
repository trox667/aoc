import unittest
import hashlib


class GenNumber:
    def __init__(self):
        self.number = 0

    def next(self):
        self.number += 1
        return self.number


def five_zeroes(hex):
    if hex[0:5] == '00000':
        return True
    else:
        return False


def gen_input(input, n):
    return input + str(n)


def gen_hash(input, gen_number):
    n = gen_number.next()
    h = hashlib.md5(gen_input(input, n).encode('ascii'))
    if five_zeroes(h.hexdigest()):
        return n
    else:
        return 0


def run(input):
    gen_number = GenNumber()
    n = gen_hash(input, gen_number)
    while n == 0:
        n = gen_hash(input, gen_number)
    return n


def part1():
    print(run('ckczppom'))


class Part1(unittest.TestCase):
    def test_five_zeroes(self):
        self.assertTrue(five_zeroes('00000'))
        self.assertFalse(five_zeroes('a0000'))

    def test_gen_number(self):
        gen = GenNumber()
        self.assertEqual(gen.next(), 1)
        self.assertEqual(gen.next(), 2)

    def test_gen_input(self):
        gen = GenNumber()
        self.assertEqual(gen_input('a', gen.next()), 'a1')
        self.assertEqual(gen_input('abc', gen.next()), 'abc2')

    def test_hash(self):
        self.assertEqual(run('abcdef'), 609043)
        self.assertEqual(run('pqrstuv'), 1048970)


if __name__ == '__main__':
    part1()
    unittest.main()
