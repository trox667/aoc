fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn read_input() -> Vec<String> {
    include_str!("../../inputs/input05")
        .lines()
        .map(|line| {
            line.replace("F", "0")
                .replace("B", "1")
                .replace("L", "0")
                .replace("R", "1")
        })
        .collect::<Vec<_>>()
}

fn part1() -> usize {
    read_input()
        .iter()
        .map(|line| {
            let row = line.chars().take(7).collect::<String>();
            let column = line.chars().skip(7).take(3).collect::<String>();
            let row = usize::from_str_radix(&row, 2).unwrap_or(0);
            let column = usize::from_str_radix(&column, 2).unwrap_or(0);
            row * 8 + column
        })
        .max()
        .unwrap_or(0)
}

fn part2() -> usize {
    let mut seat_ids = read_input()
        .iter()
        .map(|line| {
            let row = line.chars().take(7).collect::<String>();
            let column = line.chars().skip(7).take(3).collect::<String>();
            let row = usize::from_str_radix(&row, 2).unwrap_or(0);
            let column = usize::from_str_radix(&column, 2).unwrap_or(0);
            row * 8 + column
        })
        .collect::<Vec<_>>();
    seat_ids.sort();
    for seat_id in &seat_ids {
        let mid = &seat_ids.contains(&(seat_id + 1));
        let right = &seat_ids.contains(&(seat_id + 2));
        if !*mid && *right {
            return seat_id + 1;
        }
    }
    0
}

mod tests {
    use super::*;

    #[test]
    fn test_() {}
}
