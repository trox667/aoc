fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn read_input() -> Vec<&'static str> {
    include_str!("../../inputs/input03")
        .lines()
        .collect::<Vec<_>>()
}

fn run(grid: &Vec<&'static str>, step_x: usize, step_y: usize) -> usize {
    let mut hits = 0;
    let mut x = 0;
    let mut y = step_y;
    while y < grid.len() {
        x = (x + step_x) % grid[y].len();
        if grid[y].chars().nth(x).unwrap() == '#' {
            hits += 1;
        }
        y += step_y;
    }
    hits
}

fn part1() -> usize {
    run(&read_input(), 3, 1)
}

fn part2() -> usize {
    let input = read_input();
    run(&input, 1, 1)
        * run(&input, 3, 1)
        * run(&input, 5, 1)
        * run(&input, 7, 1)
        * run(&input, 1, 2)
}

mod tests {
    use super::*;

    #[test]
    fn test_() {}
}
