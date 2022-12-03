use anyhow::Result;

fn get_priority(c: char) -> usize {
    match c {
        'a'..='z' => (1 + (c as u8) - b'a') as usize,
        'A'..='Z' => (27 + (c as u8) - b'A') as usize,
        _ => 0,
    }
}

fn main() -> Result<()> {
    let content = include_str!("../../inputs/input3");
    let part1: usize = content
        .lines()
        .map(|line| {
            let mut priority = 0;
            let (first, second) = line.split_at(line.len() / 2);
            for c in first.chars() {
                if second.contains(c) {
                    priority += get_priority(c);
                    break;
                }
            }
            return priority;
        })
        .sum();
    println!("Part 1: {part1}");

    let part2: usize = content
        .lines()
        .step_by(3)
        .zip(
            content
                .lines()
                .skip(1)
                .step_by(3)
                .zip(content.lines().skip(2).step_by(3)),
        )
        .map(|tokens| {
            let first = tokens.0;
            let second = tokens.1 .0;
            let third = tokens.1 .1;
            let mut priority = 0;
            for c in first.chars() {
                if second.contains(c) && third.contains(c) {
                    priority += get_priority(c);
                    break;
                }
            }
            return priority;
        })
        .sum();
    println!("Part 2: {part2}");

    Ok(())
}
