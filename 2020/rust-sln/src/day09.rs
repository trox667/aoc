use combinations::Combinations;
fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn parse(input: &str) -> Vec<usize> {
    input
        .lines()
        .flat_map(|line| line.parse::<usize>())
        .collect::<Vec<_>>()
}

fn is_valid(nums: &Vec<usize>, target: usize) -> bool {
    let combinations = Combinations::new(nums.clone(), 2);
    for combination in combinations {
        let s: usize = combination.iter().sum();
        if s == target {
            return true;
        }
    }
    false
}

fn read_input() -> &'static str {
    include_str!("../../inputs/input09")
}

fn run(nums: &Vec<usize>, preamble: usize) -> usize {
    for i in 0..(nums.len() - preamble) {
        let end = i + preamble;
        let n = &nums[i..end];
        let target = nums[end];
        if !is_valid(&n.to_vec(), target) {
            return target;
        }
    }
    0
}

fn part1() -> usize {
    run(&parse(read_input()), 25)
}

fn run2(nums: &Vec<usize>, target: usize) -> usize {
    for i in 0..(nums.len()) {
        for j in i + 1..(nums.len()) {
            let s: usize = nums[i..j].iter().sum();
            if s == target {
                return nums[i..j].iter().min().expect("could not get a min value")
                    + nums[i..j].iter().max().expect("could not get a max value");
            } else if s > target {
                break;
            }
        }
    }
    0
}

fn part2() -> usize {
    run2(&parse(read_input()), 88311122)
}

mod tests {
    use super::*;

    fn test_input() -> &'static str {
        r#"35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"#
    }

    #[test]
    fn test_is_valid() {
        let nums: Vec<_> = (1..26).collect();
        assert!(is_valid(&nums, 26));
        assert!(is_valid(&nums, 49));
        assert!(!is_valid(&nums, 100));
        assert!(!is_valid(&nums, 50));
    }

    #[test]
    fn test_run() {
        assert_eq!(run(&parse(test_input()), 5), 127);
    }

    fn test_input2() -> &'static str {
        r#"35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"#
    }

    #[test]
    fn test_run2() {
        assert_eq!(run2(&parse(test_input2()), 127), 62);
    }
}
