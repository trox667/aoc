use std::fs;

mod day4;
mod day7;
mod day9;

#[allow(dead_code)]
fn read_file(file_path: &str) -> Vec<String> {
    let contents = fs::read_to_string(file_path).expect(format!("Could not open file. {}", file_path).as_str());
    contents.lines().filter(|line| { !line.is_empty() }).map(|line| { String::from(line) }).collect()
}

fn main() {
    {
        let lines = read_file("../inputs/input04");
        println!("Day 4 - Part1: {}", day4::part1(&lines));
        println!("Day 4 - Part2: {}", day4::part2(&lines));
    }
    {
        let lines = read_file("../inputs/input07");
        println!("Day 7 - Part1: {}", day7::part1(&lines));
        println!("Day 7 - Part2: {}", day7::part2(&lines));
    }
    {
        let lines = read_file("../inputs/input09");
        println!("Day 9 - Part1: {}", day9::part1(&lines));
        println!("Day 9 - Part2: {}", day9::part2(&lines));
    }
}
