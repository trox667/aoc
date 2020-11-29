fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn direction(c: char) -> isize {
    match c {
        '(' => 1,
        ')' => -1,
        _ => 0,
    }
}

fn path(p: &str) -> isize {
    p.chars().map(|c| direction(c)).sum()
}

fn read_input() -> &'static str {
    include_str!("../../inputs/input01")
}

fn part1() -> isize {
    path(read_input())
}

fn path2(p: &str) -> isize {
    let mut index = 1;
    let mut sum = 0;
    let directions: Vec<isize> = p.chars().map(|c| direction(c)).collect();
    for d in directions {
        sum += d;
        if sum == -1 {
            return index;
        } else {
            index += 1;
        }
    }
    0
}

fn part2() -> isize {
    path2(read_input())
}

mod tests {
    use super::*;

    #[test]
    fn test_direction() {
        assert_eq!(direction('('), 1);
        assert_eq!(direction(')'), -1);
        assert_eq!(direction('a'), 0);
    }

    #[test]
    fn test_path() {
        assert_eq!(path("abcd"), 0);
        assert_eq!(path(""), 0);
        assert_eq!(path("(())"), 0);
        assert_eq!(path("()()"), 0);
        assert_eq!(path("((("), 3);
        assert_eq!(path("(()(()("), 3);
        assert_eq!(path("))((((("), 3);
        assert_eq!(path("())"), -1);
        assert_eq!(path("))("), -1);
        assert_eq!(path(")))"), -3);
        assert_eq!(path(")())())"), -3);
    }

    #[test]
    fn test_path2() {
        assert_eq!(path2(")"), 1);
        assert_eq!(path2("()())"), 5);
    }
}
