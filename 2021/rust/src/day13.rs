use std::collections::HashSet;

type Instruction = (char, isize);
type Point = (isize, isize);
fn create_instructions_coords(lines: &Vec<String>) -> (Vec<Instruction>, Vec<Point>) {
    let mut instructions = vec![];
    let mut coords = vec![];
    for line in lines {
        if line.is_empty() {
            continue;
        } else if line.starts_with("fold") {
            let direction: Vec<&str> = line.split('=').collect();
            if direction[0].ends_with("y") {
                instructions.push(('y', direction[1].parse::<isize>().unwrap()));
            } else {
                instructions.push(('x', direction[1].parse::<isize>().unwrap()));
            }
        } else {
            let xy: Vec<&str> = line.split(',').collect();
            coords.push((
                xy[0].parse::<isize>().unwrap(),
                xy[1].parse::<isize>().unwrap(),
            ));
        }
    }
    (instructions, coords)
}

fn print_coords(coords: &Vec<Point>) {
    let maxx = coords.iter().max_by_key(|coord| coord.0).unwrap();
    let maxy = coords.iter().max_by_key(|coord| coord.1).unwrap();
    for y in 0..=maxy.1 {
        for x in 0..=maxx.0 {
            if coords.contains(&(x, y)) {
                print!("#");
            } else {
                print!(".");
            }
        }
        println!();
    }
}

fn fold(instruction: &Instruction, coords: &Vec<Point>) -> Vec<Point> {
    let mut result = HashSet::<Point>::new();
    for (x, y) in coords {
        let value = instruction.1;
        if instruction.0 == 'y' {
            result.insert((*x, value - (y - value).abs()));
        } else {
            result.insert((value - (x - value).abs(), *y));
        }
    }
    Vec::from_iter(result.into_iter())
}

pub fn part1(lines: &Vec<String>) -> usize {
    let (instructions, mut coords) = create_instructions_coords(lines);
    for instruction in instructions {
        coords = fold(&instruction, &coords);
        break;
    }
    coords.len()
}

pub fn part2(lines: &Vec<String>) -> usize {
    let (instructions, mut coords) = create_instructions_coords(lines);
    for instruction in instructions {
        coords = fold(&instruction, &coords);
    }
    print_coords(&coords);
    0
}
