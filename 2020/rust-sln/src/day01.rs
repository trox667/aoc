use combinations::Combinations;

fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn is_2020(combinations: &Vec<usize>) -> bool {
    if let Some(_) = combinations.iter().find(|x| **x == 0) {
        return false;
    }

    return combinations.iter().map(|x| *x).sum::<usize>() == 2020;
}

fn run(items: &Vec<usize>, size: usize) -> usize {
    for combination in Combinations::new(items.clone(), size) {
        if is_2020(&combination) {
            return combination.iter().fold(1, |acc, x| acc * *x);
        }
    }
    0
}

fn read_input() -> Vec<usize> {
    include_str!("../../inputs/input01")
        .lines()
        .flat_map(|line| line.parse::<usize>())
        .collect()
}

fn part1() -> usize {
    run(&read_input(), 2)
}

fn part2() -> usize {
    run(&read_input(), 3)
}

mod tests {
    use super::*;

    #[test]
    fn test_is_2020() {
        assert!(is_2020(&vec![1721, 299]));
        assert!(!is_2020(&vec![0, 1]));
        assert!(!is_2020(&vec![1900, 110]));
    }

    #[test]
    fn test_run() {
        assert_eq!(run(&vec![1, 1721, 299], 2), 514579);
        assert_eq!(run(&vec![0, 1721, 2, 299], 2), 514579);
    }
}
