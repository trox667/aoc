use std::collections::{HashMap, HashSet};

fn part1() {
    let input = "abbhdwsy";
    let mut index = 0;
    let mut result = vec![];
    for n in 0..8 {
        loop {
            let digest = md5::compute(format!("{}{}", input, index));
            let hash = format!("{:x}", digest);
            if hash.starts_with("00000") {
                let token = hash.chars().nth(5).unwrap();
                result.push(token.to_string());
                index += 1;
                break;
            } else {
                index += 1;
            }
        }
    }

    println!("Part 1: {}", result.join(""));
}

fn part2() {
    let input = "abbhdwsy";
    let mut index = 0;
    let mut result = [' '; 8];
    let mut found_results: HashSet<usize> = HashSet::new();
    loop {
        loop {
            let digest = md5::compute(format!("{}{}", input, index));
            let hash = format!("{:x}", digest);
            if hash.starts_with("00000") {
                let position = hash
                    .chars()
                    .nth(5)
                    .unwrap()
                    .to_string()
                    .parse::<usize>()
                    .unwrap_or(9);

                let token = hash.chars().nth(6).unwrap();
                if position < 8 && !found_results.contains(&position) {
                    println!("idx {}: {} - {}", index, position, token);
                    found_results.insert(position);
                    result[position] = token;
                }

                index += 1;
                break;
            } else {
                index += 1;
            }
        }
        if found_results.len() == 8 {
            println!("Part 2: {}", result.iter().collect::<String>());
            return;
        }
    }
}

fn main() {
    // part1();
    part2();
}
