import unittest
import math
import os


def module_fuel(mass):
    return math.floor(mass / 3.0) - 2


def part1():
    res = 0
    with open('input01') as input:
        res = sum([module_fuel(float(mass)) for mass in input if mass])
    return res


def total_module_fuel(mass):
    total = 0
    prev_fuel = mass
    while prev_fuel > 0:
        prev_fuel = module_fuel(prev_fuel)
        if prev_fuel > 0:
            total = total + prev_fuel
    return total


def part2():
    with open('input01') as input:
        res = sum([total_module_fuel(module_fuel(float(mass)))
                   for mass in input if mass])
    return part1() + res


class Day1Tests(unittest.TestCase):
    def test_module_fuel(self):
        self.assertEqual(module_fuel(12), 2)
        self.assertEqual(module_fuel(14), 2)
        self.assertEqual(module_fuel(1969), 654)
        self.assertEqual(module_fuel(100756), 33583)

    def test_total_module_fuel(self):
        self.assertEqual(total_module_fuel(14), 2)
        self.assertEqual(total_module_fuel(1969), 966)
        self.assertEqual(total_module_fuel(100756), 50346)


if __name__ == '__main__':
    print(part1())
    print(part2())
    unittest.main()
