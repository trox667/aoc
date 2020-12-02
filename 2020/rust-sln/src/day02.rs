use regex::Regex;
use std::error::Error;
use std::fmt;
use std::num::ParseIntError;
use std::str::FromStr;

fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

#[derive(Debug, Clone)]
struct ParseEntryError;
impl Error for ParseEntryError {}
impl fmt::Display for ParseEntryError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Could not parse to Entry")
    }
}
impl From<ParseIntError> for ParseEntryError {
    fn from(_err: ParseIntError) -> ParseEntryError {
        ParseEntryError
    }
}

#[derive(Debug, Default, PartialEq)]
struct Entry {
    c: char,
    password: String,
    range: (usize, usize),
}

impl FromStr for Entry {
    type Err = ParseEntryError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let re = Regex::new(r"(?P<min>\d+)-(?P<max>\d+) (?P<c>[A-z]): (?P<password>[A-z]+)")
            .expect("Could not create regex");
        let mut entries = vec![];
        for caps in re.captures_iter(s) {
            entries.push(Entry {
                password: caps["password"].to_string(),
                range: (
                    caps["min"].parse::<usize>().expect("Could not parse min"),
                    caps["max"].parse::<usize>().expect("Could not parse max"),
                ),
                c: caps["c"].chars().nth(0).expect("Could not get a char"),
            });
        }
        if entries.len() > 0 {
            Ok(entries.pop().expect("Entry could not be parsed"))
        } else {
            Err(ParseEntryError)
        }
    }
}

fn char_count(password: &str, c: char) -> usize {
    password.matches(c).count()
}

fn policy_minmax(entry: &Entry) -> bool {
    let min = entry.range.0;
    let max = entry.range.1;
    let count = char_count(&entry.password, entry.c);
    min <= count && count <= max
}

fn match_policy(entry: &Entry, policy: fn(&Entry) -> bool) -> bool {
    return policy(entry);
}

fn run(entries: &Vec<Entry>, policy: fn(&Entry) -> bool) -> usize {
    entries
        .iter()
        .filter(|entry| match_policy(entry, policy))
        .count()
}

fn read_input() -> Vec<Entry> {
    include_str!("../../inputs/input02")
        .lines()
        .flat_map(|line| Entry::from_str(line))
        .collect::<Vec<_>>()
}

fn part1() -> usize {
    run(&read_input(), policy_minmax)
}

fn char_pos(password: &str, c: char, pos: usize) -> bool {
    if let Some(tc) = password.chars().nth(pos - 1) {
        return tc == c;
    }
    false
}

fn policy_position(entry: &Entry) -> bool {
    char_pos(&entry.password, entry.c, entry.range.0)
        ^ char_pos(&entry.password, entry.c, entry.range.1)
}

fn part2() -> usize {
    run(&read_input(), policy_position)
}

mod tests {
    use super::*;

    #[test]
    fn test_parse() {
        assert_eq!(
            Entry::from_str("1-3 a: abcde").unwrap(),
            Entry {
                c: 'a',
                password: "abcde".into(),
                range: (1, 3)
            }
        )
    }

    #[test]
    fn test_char_count() {
        assert_eq!(char_count("abcde", 'a'), 1);
        assert_eq!(char_count("cdefg", 'b'), 0);
        assert_eq!(char_count("ccccccccc", 'c'), 9);
    }

    #[test]
    fn test_policy_minmax() {
        assert!(policy_minmax(&Entry {
            password: "abcde".into(),
            c: 'a',
            range: (1, 3)
        }));
    }

    #[test]
    fn test_run() {
        let list = vec![
            Entry {
                password: "abcde".into(),
                c: 'a',
                range: (1, 3),
            },
            Entry {
                password: "cdefg".into(),
                c: 'b',
                range: (1, 3),
            },
            Entry {
                password: "ccccccccc".into(),
                c: 'c',
                range: (2, 9),
            },
        ];
        assert_eq!(run(&list, policy_minmax), 2);
    }

    #[test]
    fn test_policy_position() {
        assert!(policy_position(&Entry {
            password: "abcde".into(),
            c: 'a',
            range: (1, 3)
        }));
    }
}
