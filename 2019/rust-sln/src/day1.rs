fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn read_input() -> Vec<i32> {
    include_str!("../input01")
        .split_terminator('\n')
        .flat_map(|s| s.parse::<i32>())
        .collect::<_>()
}

fn calc_mass(f: i32) -> i32 {
    (f as f32 / 3.0).floor() as i32 - 2
}

fn total_mass(f: i32) -> i32 {
    match calc_mass(f) {
        nf if nf > 0 => f + total_mass(nf),
        _ => f,
    }
}

fn part1() -> i32 {
    read_input().iter().map(|n| calc_mass(*n)).sum()
}

fn part2() -> i32 {
    read_input()
        .iter()
        .map(|n| total_mass(calc_mass(*n)))
        .sum::<i32>()
}

mod tests {
    use super::*;

    #[test]
    fn test_calc_mass() {
        assert_eq!(calc_mass(12), 2);
        assert_eq!(calc_mass(14), 2);
        assert_eq!(calc_mass(1969), 654);
        assert_eq!(calc_mass(100756), 33583);
    }

    #[test]
    fn test_total_mass() {
        assert_eq!(total_mass(2), 2);
        assert_eq!(total_mass(654), 966);
        assert_eq!(total_mass(33583), 50346);
    }
}
