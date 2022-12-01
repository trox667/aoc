use anyhow::Result;
use std::fs;

fn main() -> Result<()> {
    let contents = fs::read_to_string("../inputs/input1")?;

    let mut sums: Vec<u64> = contents
        .split("\n\n")
        .map(|line| {
            line.split("\n")
                .filter_map(|line| line.parse::<u64>().ok())
                .sum()
        })
        .collect();

    sums.sort();
    let last = sums.last().expect("No sums, corrupted input?");
    println!("Part 1: {last}");

    sums.reverse();
    let top_three: u64 = sums.into_iter().take(3).sum();
    println!("Part 2: {top_three}");

    Ok(())
}
