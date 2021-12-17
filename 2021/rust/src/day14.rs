use std::collections::HashMap;

type Rules = HashMap<String, Vec<String>>;
type PairsCount = HashMap<String, u64>;

fn create_rules(lines: &Vec<String>) -> Rules {
    let mut rules = Rules::new();
    lines.iter().skip(1).for_each(|line| {
        let key = &line[0..2];
        let val = &line[6..7].chars().nth(0).unwrap();
        let a = key.chars().nth(0).unwrap();
        let b = key.chars().nth(1).unwrap();
        rules.insert(
            key.to_owned(),
            vec![format!("{}{}", a, val), format!("{}{}", val, b)],
        );
    });
    rules
}

fn init(polymer: &String) -> PairsCount {
    let mut pair_count = PairsCount::new();
    for i in 2..=polymer.len() {
        let pair = &polymer[(i - 2)..i].to_owned();
        *pair_count.entry(pair.clone()).or_insert(0) += 1;
    }
    pair_count
}

fn count(pairs_count: &PairsCount, last_element: char) -> u64 {
    let mut element_count = HashMap::<char, u64>::new();
    for (key, count) in pairs_count {
        *element_count
            .entry(key.chars().nth(0).unwrap())
            .or_insert(0) += count;
    }
    *element_count.get_mut(&last_element).unwrap() += 1;

    let mut min_count = u64::MAX;
    let mut max_count = 0;
    for (_, count) in element_count {
        min_count = min_count.min(count);
        max_count = max_count.max(count);
    }
    max_count - min_count
}

fn next_step(pairs_count: &PairsCount, rules: &Rules) -> PairsCount {
    let mut new_pairs_count = PairsCount::new();
    for (key, count) in pairs_count {
        let combinations = rules.get(key).unwrap();
        for combination in combinations {
            *new_pairs_count.entry(combination.clone()).or_insert(0) += count;
        }
    }
    new_pairs_count
}

fn run(lines: &Vec<String>, steps: usize) -> u64 {
    let polymer = &lines[0];
    let rules = create_rules(lines);
    let mut pairs_count = init(polymer);
    for _ in 0..steps {
        pairs_count = next_step(&pairs_count, &rules);
    }
    count(&pairs_count, polymer.chars().last().unwrap())
}

pub fn part1(lines: &Vec<String>) -> u64 {
    run(lines, 10)
}

pub fn part2(lines: &Vec<String>) -> u64 {
    run(lines, 40)
}
