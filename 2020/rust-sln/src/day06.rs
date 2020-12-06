use std::collections::HashSet;

fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn read_input() -> Vec<Vec<String>> {
    include_str!("../../inputs/input06")
        .split("\n\n")
        .map(|s| {
            s.split("\n")
                .map(|s| s.to_owned())
                .filter(|s| !s.is_empty())
                .collect::<Vec<String>>()
        })
        .collect::<Vec<_>>()
}

fn part1() -> usize {
    let mut count = 0;
    read_input().iter().for_each(|answers| {
        let mut sets: Vec<HashSet<_>> = vec![];
        for answer in answers {
            sets.push(answer.chars().collect());
        }
        let union = sets
            .iter()
            .fold(HashSet::new(), |acc, hs| acc.union(hs).cloned().collect());
        count += union.len();
    });
    count
}

fn part2() -> usize {
    let mut count = 0;
    read_input().iter().for_each(|answers| {
        let mut sets: Vec<HashSet<_>> = vec![];
        for answer in answers {
            sets.push(answer.chars().collect());
        }
        let intersection = sets.iter().skip(1).fold(sets[0].clone(), |acc, hs| {
            acc.intersection(hs).cloned().collect()
        });
        count += intersection.len();
    });
    count
}

mod tests {
    use super::*;

    #[test]
    fn test_() {}
}
