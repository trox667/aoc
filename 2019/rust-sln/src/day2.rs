fn main() {
    println!("{}", part1());
}

fn read_input() -> Vec<usize> {
    include_str!("../input02")
        .split(',')
        .flat_map(|n| n.parse::<usize>())
        .collect()
}

#[derive(PartialEq)]
enum OpCode {
    READ,
    ADD = 1,
    MUL = 2,
    HALT = 99,
}

fn op(opcode: usize) -> OpCode {
    match opcode {
        1 => OpCode::ADD,
        2 => OpCode::MUL,
        99 => OpCode::HALT,
        _ => OpCode::READ,
    }
}

fn read(program: &Vec<usize>, position: usize) -> usize {
    program[position]
}

fn add(program: &mut Vec<usize>, position: usize) -> usize {
    let position_a = read(program, position);
    let position_b = read(program, position + 1);
    let position_c = read(program, position + 2);
    program[position_c] = read(program, position_a) + read(program, position_b);
    position + 3
}

fn mul(program: &mut Vec<usize>, position: usize) -> usize {
    let position_a = read(program, position);
    let position_b = read(program, position + 1);
    let position_c = read(program, position + 2);
    program[position_c] = read(program, position_a) * read(program, position_b);
    position + 3
}

fn run(program: &mut Vec<usize>, start: usize, read_pos: usize) -> usize {
    let mut position = start;
    let mut state = OpCode::READ;
    while state != OpCode::HALT {
        match state {
            OpCode::READ => {
                state = op(read(program, position));
                position += 1;
            }
            OpCode::ADD => {
                state = OpCode::READ;
                position = add(program, position);
            }
            OpCode::MUL => {
                state = OpCode::READ;
                position = mul(program, position);
            }
            _ => {}
        }
    }

    program[read_pos]
}

fn part1() -> usize {
    let mut program = read_input();
    program[1] = 12;
    program[2] = 2;
    run(&mut program, 0, 0)
}

mod test {
    use super::*;

    #[test]
    fn test_read() {
        let program = vec![1, 0, 0, 3, 99];
        assert_eq!(read(&program, 0), 1);
    }

    #[test]
    fn test_add() {
        let mut program = vec![1, 0, 0, 3, 99];
        add(&mut program, 1);
        assert_eq!(program[3], 2);
    }

    #[test]
    fn test_mul() {
        let mut program = vec![1, 0, 0, 3, 99];
        mul(&mut program, 1);
        assert_eq!(program[3], 1);
    }

    #[test]
    fn test_run() {
        let mut program = vec![1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];
        assert_eq!(run(&mut program, 0, 0), 3500);

        let mut program = vec![1, 0, 0, 0, 99];
        assert_eq!(run(&mut program, 0, 0), 2);

        let mut program = vec![2, 3, 0, 3, 99];
        assert_eq!(run(&mut program, 0, 3), 6);

        let mut program = vec![2, 4, 4, 5, 99, 0];
        assert_eq!(run(&mut program, 0, 5), 9801);

        let mut program = vec![1, 1, 1, 4, 99, 5, 6, 0, 99];
        assert_eq!(run(&mut program, 0, 0), 30);
    }
}
