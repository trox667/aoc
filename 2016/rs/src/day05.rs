use std::collections::HashSet;
use std::sync::mpsc;
use std::thread;

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

fn part1_mt() {
    let input = "abbhdwsy";

    let thread_count = 100;
    let max = 100_000_000;

    let (tx, rx) = mpsc::channel();
    let range = max / thread_count;

    let _threads: Vec<_> = (0..thread_count)
        .map(|i| {
            let tx = tx.clone();
            thread::spawn(move || {
                let mut result = vec![];

                let start = i * range;
                let end = (i + 1) * range - 1;
                for index in start..end {
                    let digest = md5::compute(format!("{}{}", input, index));
                    let hash = format!("{:x}", digest);
                    if hash.starts_with("00000") {
                        let token = hash.chars().nth(5).unwrap();
                        result.push(token.to_string());
                    }
                }
                tx.send((i, result)).unwrap();
            })
        })
        .collect();

    // close the threads as soon as all transmissions finished
    drop(tx);

    let mut thread_result = vec![];
    for received in rx {
        thread_result.push(received);
        // println!("Got {:?}", received);
    }

    let mut tmp = thread_result
        .iter()
        .filter(|(_, data)| !data.is_empty())
        .collect::<Vec<_>>();
    tmp.sort_by(|(id1, _), (id2, _)| id1.partial_cmp(id2).unwrap());
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
    // part2();

    part1_mt();
}
