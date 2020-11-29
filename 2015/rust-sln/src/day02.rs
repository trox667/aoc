fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn read_input() -> &'static str {
    include_str!("../../inputs/input02")
}

fn box_paper(l: usize, w: usize, h: usize) -> usize {
    let area_a = l * w;
    let area_b = l * h;
    let area_c = w * h;
    area_a.min(area_b.min(area_c)) + 2 * area_a + 2 * area_b + 2 * area_c
}

type BoxSize = (usize, usize, usize);
fn line_to_tuple(line: &str) -> BoxSize {
    let values = line
        .split('x')
        .flat_map(|i| i.parse::<usize>())
        .take(3)
        .collect::<Vec<_>>();
    (values[0], values[1], values[2])
}

fn part1() -> usize {
    read_input()
        .lines()
        .map(|line| line_to_tuple(line))
        .map(|v| box_paper(v.0, v.1, v.2))
        .sum()
}

fn volume(w: usize, l: usize, h: usize) -> usize {
    w * l * h
}

fn smallest_perimeter(w: usize, l: usize, h: usize) -> usize {
    let a = l + w;
    let b = l + h;
    let c = w + h;
    2 * a.min(b.min(c))
}

fn ribbon(w: usize, l: usize, h: usize) -> usize {
    smallest_perimeter(w, l, h) + volume(w, l, h)
}

fn part2() -> usize {
    read_input()
        .lines()
        .map(|line| line_to_tuple(line))
        .map(|v| ribbon(v.0, v.1, v.2))
        .sum()
}

mod tests {
    use super::*;

    #[test]
    fn test_box_paper() {
        assert_eq!(box_paper(2, 3, 4), 58);
        assert_eq!(box_paper(1, 1, 10), 43);
        assert_eq!(box_paper(0, 0, 1), 0);
    }

    #[test]
    fn test_line_to_tuple() {
        assert_eq!(line_to_tuple("2x3x4"), (2, 3, 4));
    }

    #[test]
    fn test_volume() {
        assert_eq!(volume(2, 3, 4), 24);
        assert_eq!(volume(1, 1, 10), 10);
    }

    #[test]
    fn test_smallest_perimeter() {
        assert_eq!(smallest_perimeter(2, 3, 4), 10);
        assert_eq!(smallest_perimeter(1, 1, 10), 4);
    }

    #[test]
    fn test_ribbon() {
        assert_eq!(ribbon(2, 3, 4), 34);
        assert_eq!(ribbon(1, 1, 10), 14);
    }
}
