use std::collections::HashSet;
fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn read_input() -> Vec<(&'static str, isize)> {
    include_str!("../../inputs/input08")
        .split('\n')
        .filter(|line| line.len() > 0)
        .map(|line| parse(line))
        .collect::<Vec<_>>()
}

fn parse<'a>(line: &'a str) -> (&'a str, isize) {
    let tokens = line.trim().split(' ').collect::<Vec<_>>();
    (tokens[0], tokens[1].parse::<isize>().unwrap())
}

#[derive(Debug, PartialEq, Clone)]
enum State {
    Infinite,
    Finished,
    Error,
}

fn step(instructions: &Vec<(&str, isize)>, pointer: isize, acc: isize) -> (isize, isize) {
    let (op, count) = instructions[pointer as usize];
    match op {
        "acc" => (pointer + 1, acc + count),
        "jmp" => (pointer + count, acc),
        _ => (pointer + 1, acc),
    }
}

fn out_of_bounds(pointer: isize, size: isize) -> bool {
    pointer >= size
}

fn run(instructions: &Vec<(&str, isize)>) -> (State, isize) {
    let mut visited = HashSet::new();
    let mut pointer = 0;
    let mut acc = 0;
    loop {
        if visited.get(&pointer).is_some() {
            return (State::Infinite, acc);
        }
        visited.insert(pointer);
        let (p, a) = step(instructions, pointer, acc);
        pointer = p;
        acc = a;
        if out_of_bounds(pointer, instructions.len() as isize) {
            return (State::Finished, acc);
        }
    }
}

fn part1() -> isize {
    let (state, acc) = run(&read_input());
    assert_eq!(state, State::Infinite);
    acc
}

fn replace_op(pointer: usize, instructions: &mut Vec<(&str, isize)>) {
    match instructions[pointer].0 {
        "nop" => instructions[pointer] = ("jmp", instructions[pointer].1),
        "jmp" => instructions[pointer] = ("nop", instructions[pointer].1),
        _ => (),
    };
}

fn run2(instructions: &Vec<(&str, isize)>) -> (State, isize) {
    for pointer in 0..instructions.len() {
        let mut curr_instructions = instructions.clone();
        replace_op(pointer, &mut curr_instructions);
        let (state, acc) = run(&curr_instructions);
        if state == State::Finished {
            return (state, acc);
        }
    }

    (State::Error, 0)
}

fn part2() -> isize {
    let (state, acc) = run2(&read_input());
    assert_eq!(state, State::Finished);
    acc
}

mod tests {
    use super::*;

    fn test_input() -> &'static str {
        r#"nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"#
    }

    #[test]
    fn test_parse() {
        let input = test_input().split('\n').collect::<Vec<_>>();
        assert_eq!(parse(input[0]), ("nop", 0));
        assert_eq!(parse(input[1]), ("acc", 1));
        assert_eq!(parse(input[2]), ("jmp", 4));
    }

    #[test]
    fn test_step() {
        let instructions = test_input()
            .split('\n')
            .map(|line| parse(line))
            .collect::<Vec<_>>();
        let pointer = 0;
        let acc = 0;
        assert_eq!(step(&instructions, pointer, acc), (1, 0));
        let pointer = 1;
        let acc = 0;
        assert_eq!(step(&instructions, pointer, acc), (2, 1));
        let pointer = 2;
        let acc = 1;
        assert_eq!(step(&instructions, pointer, acc), (6, 1));
        let pointer = 6;
        let acc = 1;
        assert_eq!(step(&instructions, pointer, acc), (7, 2));
    }

    #[test]
    fn test_run() {
        let instructions = test_input()
            .split('\n')
            .map(|line| parse(line))
            .collect::<Vec<_>>();
        assert_eq!(run(&instructions), (State::Infinite, 5));
    }
}
