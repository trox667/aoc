import unittest
import re


def parse_passport(line):
    items = dict()
    pairs = line.split(' ')
    for pair in pairs:
        k, v = pair.split(':')
        items[k] = v
    return items


def to_single_line(lines):
    passports = list()
    curr_str = ''
    for line in lines:
        if not line.isspace() and not len(line) == 0:
            curr_str += line.strip() + ' '
        else:
            passports.append(curr_str.rstrip())
            curr_str = ''
    if len(curr_str) > 0:
        passports.append(curr_str.rstrip())
    return passports


def validate_passport(passport):
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
        return True
    else:
        return False


def validate_values(passport):
    result = True
    for k, v in passport.items():
        if not result:
            break
        if k == 'byr':
            result = 1920 <= int(v) <= 2002
        elif k == 'iyr':
            result = 2010 <= int(v) <= 2020
        elif k == 'eyr':
            result = 2020 <= int(v) <= 2030
        elif k == 'hgt':
            pattern = r'(\d+)([a-z]+)'
            matches = re.search(pattern, v)
            if not matches:
                result = False
            else:
                if matches.group(2) == 'cm':
                    result = 150 <= int(matches.group(1)) <= 193
                elif matches.group(2) == 'in':
                    result = 59 <= int(matches.group(1)) <= 76
                else:
                    result = False
        elif k == 'hcl':
            pattern = r'#([0-9]|[a-f]){6}'
            matches = re.match(pattern, v)
            if not matches:
                result = False
            elif matches.group(1):
                result = True
            else:
                result = False
        elif k == 'ecl':
            pattern = r'(amb|blu|brn|gry|grn|hzl|oth)'
            matches = re.match(pattern, v)
            if not matches:
                result = False
            elif matches.group(1):
                result = True
            else:
                result = False
        elif k == 'pid':
            pattern = r'^(\d){9}$'
            matches = re.match(pattern, v)
            if not matches:
                result = False
            elif matches.group(1):
                result = True
            else:
                result = False
    return result


def run(lines):
    count = 0
    new_lines = to_single_line(lines)
    passports = [parse_passport(line) for line in new_lines]
    for passport in passports:
        if validate_passport(passport):
            count += 1
    return count


def part1():
    print(run(read_input()))


def run2(lines):
    count = 0
    new_lines = to_single_line(lines)
    passports = [parse_passport(line) for line in new_lines]
    for passport in passports:
        if validate_passport(passport) and validate_values(passport):
            count += 1
    return count


def part2():
    print(run2(read_input()))


def read_input():
    with open('../inputs/input04') as input:
        return [i.rstrip() for i in input]


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
        i = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
        self.assertEqual(len(to_single_line(i.split('\n'))), 4)

    def test_validate_password(self):
        i = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
        lines = to_single_line(i.split('\n'))
        passports = [parse_passport(line) for line in lines]
        self.assertTrue(validate_passport(passports[0]))
        self.assertFalse(validate_passport(passports[1]))
        self.assertTrue(validate_passport(passports[2]))
        self.assertFalse(validate_passport(passports[3]))

    def test_run(self):
        i = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
         byr:1937 iyr:2017 cid:147 hgt:183cm

         iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
         hcl:#cfa07d byr:1929

         hcl:#ae17e1 iyr:2013
         eyr:2024
         ecl:brn pid:760753108 byr:1931
         hgt:179cm

         hcl:#cfa07d eyr:2025 pid:166559648
         iyr:2011 ecl:brn hgt:59in"""
        lines = i.split('\n')
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
