use regex::Regex;
use std::collections::{HashMap, HashSet};

fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

type Passport = HashMap<String, String>;

fn read_input() -> &'static str {
    include_str!("../../inputs/input04")
}

fn parse_passports(input: &String) -> Vec<String> {
    input
        .split_terminator("\n\n")
        .map(|line| line.replace("\n", " ").trim().to_string())
        .collect::<Vec<_>>()
}

fn create_passport(line: &String) -> Passport {
    let mut map = HashMap::new();
    line.split_whitespace().for_each(|kv| {
        let kv = kv.split_terminator(':').collect::<Vec<_>>();
        if kv.len() >= 2 {
            map.insert(kv[0].to_string(), kv[1].to_string());
        }
    });

    map
}

fn validate_passport(passport: &Passport) -> bool {
    let mut set = HashSet::new();
    set.insert(String::from("byr"));
    set.insert(String::from("iyr"));
    set.insert(String::from("eyr"));
    set.insert(String::from("hgt"));
    set.insert(String::from("hcl"));
    set.insert(String::from("ecl"));
    set.insert(String::from("pid"));
    passport.keys().filter(|key| set.contains(*key)).count() >= 7
}

fn run1(input: &String) -> usize {
    parse_passports(input)
        .iter()
        .map(|line| create_passport(&line))
        .filter(|passport| validate_passport(&passport))
        .count()
}

fn part1() -> usize {
    parse_passports(&read_input().to_string())
        .iter()
        .map(|line| create_passport(&line))
        .filter(|passport| validate_passport(&passport))
        .count()
}

fn in_range(min: usize, max: usize, value: &str) -> bool {
    let v = value.parse::<usize>().unwrap();
    min <= v && v <= max
}

fn match_pattern(pattern: &str, value: &str) -> bool {
    let re = Regex::new(pattern).unwrap();
    re.find(value).is_some()
    // re.captures_len() >= 1
}

fn valid_byr(value: &str) -> bool {
    in_range(1920, 2002, value)
}
fn valid_iyr(value: &str) -> bool {
    in_range(2010, 2020, value)
}
fn valid_eyr(value: &str) -> bool {
    in_range(2020, 2030, value)
}
fn valid_hcl(value: &str) -> bool {
    match_pattern(r"#([0-9]|[a-f]){6}", value)
}
fn valid_ecl(value: &str) -> bool {
    match_pattern(r"(amb|blu|brn|gry|grn|hzl|oth)", value)
}
fn valid_hgt(value: &str) -> bool {
    let re = Regex::new(r"(?P<v>\d+)(?P<unit>[a-z]+)").unwrap();
    for caps in re.captures_iter(value) {
        let v = caps["v"].to_string();
        let unit = caps["unit"].to_string();
        return match unit.as_ref() {
            "cm" => in_range(150, 193, &v),
            "in" => in_range(59, 76, &v),
            _ => false,
        };
    }
    false
}
fn valid_pid(value: &str) -> bool {
    match_pattern(r"^(\d){9}$", value)
}

fn validate_values(passport: &Passport) -> bool {
    let mut result = true;
    for (k, v) in passport {
        if !result {
            return false;
        }
        result = match k.as_ref() {
            "byr" => valid_byr(v),
            "iyr" => valid_iyr(v),
            "eyr" => valid_eyr(v),
            "hcl" => valid_hcl(v),
            "ecl" => valid_ecl(v),
            "hgt" => valid_hgt(v),
            "pid" => valid_pid(v),
            _ => true,
        }
    }
    return result;
}

fn part2() -> usize {
    parse_passports(&read_input().to_string())
        .iter()
        .map(|line| create_passport(&line))
        .filter(|passport| validate_passport(&passport) && validate_values(&passport))
        .count()
}

mod tests {
    use super::*;

    fn test_input() -> String {
        r#"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"#
            .to_string()
    }

    #[test]
    fn test_parse_passports() {
        assert_eq!(parse_passports(&test_input()).len(), 4);
    }

    #[test]
    fn test_create_passport() {
        let mut ref_map: Passport = HashMap::new();
        ref_map.insert(String::from("ecl"), String::from("gry"));
        ref_map.insert(String::from("pid"), String::from("860033327"));
        ref_map.insert(String::from("byr"), String::from("1937"));
        ref_map.insert(String::from("iyr"), String::from("2017"));
        ref_map.insert(String::from("cid"), String::from("147"));
        ref_map.insert(String::from("hgt"), String::from("183cm"));
        ref_map.insert(String::from("hcl"), String::from("#fffffd"));
        ref_map.insert(String::from("eyr"), String::from("2020"));
        assert_eq!(
            create_passport(
                &"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
                    .to_string()
            ),
            ref_map
        );
    }

    #[test]
    fn test_validate_passport() {
        assert!(validate_passport(&create_passport(
            &"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
                .to_string()
        )));
    }

    #[test]
    fn test_run1() {
        assert_eq!(run1(&test_input()), 2);
    }

    #[test]
    fn test_validate_values() {
        let mut passport: Passport = HashMap::new();
        passport.insert(String::from("ecl"), String::from("gry"));
        passport.insert(String::from("pid"), String::from("860033327"));
        passport.insert(String::from("byr"), String::from("1937"));
        passport.insert(String::from("iyr"), String::from("2017"));
        passport.insert(String::from("cid"), String::from("147"));
        passport.insert(String::from("hgt"), String::from("183cm"));
        passport.insert(String::from("hcl"), String::from("#fffffd"));
        passport.insert(String::from("eyr"), String::from("2020"));
        assert!(validate_values(&passport));
        let mut passport: Passport = HashMap::new();
        passport.insert(String::from("ecl"), String::from("abc"));
        passport.insert(String::from("pid"), String::from("860033327"));
        passport.insert(String::from("byr"), String::from("1937"));
        passport.insert(String::from("iyr"), String::from("2017"));
        passport.insert(String::from("cid"), String::from("147"));
        passport.insert(String::from("hgt"), String::from("183cm"));
        passport.insert(String::from("hcl"), String::from("#fffffd"));
        passport.insert(String::from("eyr"), String::from("2020"));
        assert!(!validate_values(&passport));
        let mut passport: Passport = HashMap::new();
        passport.insert(String::from("ecl"), String::from("gry"));
        passport.insert(String::from("pid"), String::from("860033327"));
        passport.insert(String::from("byr"), String::from("1937"));
        passport.insert(String::from("iyr"), String::from("2017"));
        passport.insert(String::from("cid"), String::from("147"));
        passport.insert(String::from("hgt"), String::from("183"));
        passport.insert(String::from("hcl"), String::from("#fffffd"));
        passport.insert(String::from("eyr"), String::from("2020"));
        assert!(!validate_values(&passport));
        let mut passport: Passport = HashMap::new();
        passport.insert(String::from("ecl"), String::from("gry"));
        passport.insert(String::from("pid"), String::from("0123456789"));
        passport.insert(String::from("byr"), String::from("1937"));
        passport.insert(String::from("iyr"), String::from("2017"));
        passport.insert(String::from("cid"), String::from("147"));
        passport.insert(String::from("hgt"), String::from("183cm"));
        passport.insert(String::from("hcl"), String::from("#fffffd"));
        passport.insert(String::from("eyr"), String::from("2020"));
        assert!(!validate_values(&passport));
        let mut passport: Passport = HashMap::new();
        passport.insert(String::from("ecl"), String::from("gry"));
        passport.insert(String::from("pid"), String::from("860033327"));
        passport.insert(String::from("byr"), String::from("1937"));
        passport.insert(String::from("iyr"), String::from("2017"));
        passport.insert(String::from("cid"), String::from("147"));
        passport.insert(String::from("hgt"), String::from("183cm"));
        passport.insert(String::from("hcl"), String::from("#123abz"));
        passport.insert(String::from("eyr"), String::from("2020"));
        assert!(!validate_values(&passport));
    }
}
