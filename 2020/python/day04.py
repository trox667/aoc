import unittest
import re


def parse_passport(line):
    items = dict()
    for pair in line.split(' '):
        k, v = pair.split(':')
        items[k] = v
    return items


def to_passports(lines):
    return [block.replace('\n', ' ').strip() for block in lines.split('\n\n')]


def validate_passport(passport):
    validation_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return all(k in passport for k in validation_keys)


def in_range(min, max, value):
    return int(value) in range(min, max+1)


def make_in_range(min, max): return lambda v: in_range(min, max, v)


def match(pattern, value):
    matches = re.match(pattern, value)
    return matches and matches.group(1)


hgt_map = {'cm': make_in_range(150, 193), 'in': make_in_range(59, 76)}


def valid_byr(value): return in_range(1920, 2002, value)
def valid_iyr(value): return in_range(2010, 2020, value)
def valid_eyr(value): return in_range(2020, 2030, value)
def valid_hcl(value): return match(r'#([0-9]|[a-f]){6}', value)
def valid_ecl(value): return match(r'(amb|blu|brn|gry|grn|hzl|oth)', value)
def valid_pid(value): return match(r'^(\d){9}$', value)


def valid_hgt(value):
    matches = re.search(r'(\d+)([a-z]+)', value)
    if matches:
        v, unit = matches.group(1, 2)
        return hgt_map[unit](v)
    else:
        return False


validate_map = {'byr': valid_byr,
                'iyr': valid_iyr,
                'eyr': valid_eyr,
                'hgt': valid_hgt,
                'hcl': valid_hcl,
                'ecl': valid_ecl,
                'pid': valid_pid
                }


def validate_values(passport):
    result = True
    for k, v in passport.items():
        if not result:
            break
        if k in validate_map:
            result = validate_map[k](v)
    return result


def validate2(passport):
    return validate_passport(passport) and validate_values(passport)


def run(lines, validation_func=validate_passport):
    return len([passport for passport in [parse_passport(line) for line in to_passports(
        lines)] if validation_func(passport)])


def part1():
    print(run(read_input()))


def part2():
    print(run(read_input(), validate2))


def read_input():
    with open('../inputs/input04') as input:
        return input.read()


test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


class TestPart1(unittest.TestCase):
    def test_parse_passport(self):
        ref = {
            'ecl': 'gry',
            'pid': '860033327',
            'eyr': '2020',
            'hcl': '#fffffd',
            'byr': '1937',
            'iyr': '2017',
            'cid': '147',
            'hgt': '183cm'
        }
        self.assertEqual(
            parse_passport(
                'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
            ), ref)

    def test_to_single_line(self):
        self.assertEqual(len(to_passports(test_input)), 4)

    def test_validate_password(self):
        lines = to_passports(test_input)
        passports = [parse_passport(line) for line in lines]
        self.assertTrue(validate_passport(passports[0]))
        self.assertFalse(validate_passport(passports[1]))
        self.assertTrue(validate_passport(passports[2]))
        self.assertFalse(validate_passport(passports[3]))

    def test_run(self):
        lines = test_input
        self.assertEqual(run(lines), 2)


class TestPart2(unittest.TestCase):
    def test_validate_values(self):
        passport = {
            'byr': '2002',
            'iyr': '2015',
            'eyr': '2025',
            'hgt': '60in',
            'hcl': '#123abc',
            'ecl': 'brn',
            'pid': '000000001'
        }
        self.assertTrue(validate_values(passport))
        passport = {
            'byr': '2003',
            'iyr': '2015',
            'eyr': '2025',
            'hgt': '60in',
            'hcl': '#123abc',
            'ecl': 'brn',
            'pid': '000000001'
        }
        self.assertFalse(validate_values(passport))
        passport = {
            'byr': '2002',
            'iyr': '2015',
            'eyr': '2025',
            'hgt': '190',
            'hcl': '#123abc',
            'ecl': 'brn',
            'pid': '000000001'
        }
        self.assertFalse(validate_values(passport))
        passport = {
            'byr': '2002',
            'iyr': '2015',
            'eyr': '2025',
            'hgt': '190cm',
            'hcl': '#123abz',
            'ecl': 'brn',
            'pid': '000000001'
        }
        self.assertFalse(validate_values(passport))
        passport = {
            'byr': '2002',
            'iyr': '2015',
            'eyr': '2025',
            'hgt': '190cm',
            'hcl': '#123abc',
            'ecl': 'wat',
            'pid': '000000001'
        }
        self.assertFalse(validate_values(passport))
        passport = {
            'byr': '2002',
            'iyr': '2015',
            'eyr': '2025',
            'hgt': '190cm',
            'hcl': '#123abc',
            'ecl': 'brn',
            'pid': '1000000011'
        }
        self.assertFalse(validate_values(passport))

    def test_run2(self):
        pass


if __name__ == '__main__':
    part1()
    part2()
    unittest.main()
