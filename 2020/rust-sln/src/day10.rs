use std::collections::HashMap;

fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn parse(input: &str) -> Vec<isize> {
    input
        .lines()
        .flat_map(|line| line.trim().parse::<isize>())
        .collect()
}

fn read_input() -> &'static str {
    include_str!("../../inputs/input10")
}

fn run1(adapters: &mut Vec<isize>) -> isize {
    adapters.insert(0, 0);
    adapters.push(adapters.iter().max().expect("no entry in adapters") + 3);
    adapters.sort();
    let mut diff_one = 0;
    let mut diff_three = 0;
    for i in 0..(adapters.len() - 1) {
        let diff = adapters[i + 1] - adapters[i];
        if diff == 3 {
            diff_three += 1;
        } else if diff == 1 {
            diff_one += 1;
        }
    }
    diff_one * diff_three
}

fn part1() -> isize {
    run1(&mut parse(read_input()))
}

fn run2(adapters: &mut Vec<isize>) -> isize {
    adapters.insert(0, 0);
    adapters.sort();
    let mut all_options: HashMap<isize, isize> = HashMap::new();
    all_options.insert(0, 1);

    for i in 1..adapters.len() {
        let adapter = adapters[i];
        let pv1 = all_options.get(&(adapter - 1)).unwrap_or(&0).clone();
        let pv2 = all_options.get(&(adapter - 2)).unwrap_or(&0).clone();
        let pv3 = all_options.get(&(adapter - 3)).unwrap_or(&0).clone();
        all_options.insert(adapter, pv1 + pv2 + pv3);
    }
    *all_options
        .get(adapters.last().expect("Adapters is empty"))
        .expect("No option found")
}

fn part2() -> isize {
    run2(&mut parse(read_input()))
}

mod tests {
    use super::*;

    fn test_input() -> &'static str {
        r#"16
10
15
5
1
11
7
19
6
12
4"#
    }
    #[test]
    fn test_parse() {
        let r = vec![16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4];
        assert_eq!(parse(test_input()), r);
    }

    #[test]
    fn test_run() {
        assert_eq!(run1(&mut parse(test_input())), 35);
    }
}
