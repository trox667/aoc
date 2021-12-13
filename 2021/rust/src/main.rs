use std::fs;

mod day10;
mod day11;
mod day12;
mod day13;
mod day4;
mod day7;
mod day9;

#[allow(dead_code)]
fn read_file(file_path: &str) -> Vec<String> {
    let contents = fs::read_to_string(file_path)
        .expect(format!("Could not open file. {}", file_path).as_str());
    contents
        .lines()
        .filter(|line| !line.is_empty())
        .map(|line| String::from(line))
        .collect()
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
    {
        let lines = read_file("../inputs/input10");
        println!("Day 10 - Part1: {}", day10::part1(&lines));
        println!("Day 10 - Part2: {}", day10::part2(&lines));
    }
    {
        let lines = read_file("../inputs/input11");
        println!("Day 11 - Part1: {}", day11::part1(&lines));
        println!("Day 11 - Part2: {}", day11::part2(&lines));
    }
    {
        let lines = read_file("../inputs/input12");
        println!("Day 12 - Part1: {}", day12::part1(&lines));
        println!("Day 12 - Part2: {}", day12::part2(&lines));
    }
    {
        let lines = read_file("../inputs/input13");
        println!("Day 13 - Part1: {}", day13::part1(&lines));
        println!("Day 13 - Part2: {}", day13::part2(&lines));
    }
}
