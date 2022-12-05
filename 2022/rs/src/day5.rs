use anyhow::Result;

// TODO: this is not very rusty :(
fn main() -> Result<()> {
    let content = include_str!("../../inputs/input5");
    let lines: Vec<_> = content.lines().collect();
    let crates_count = (lines[0].len() + 2) / 4;

    let mut stacks: Vec<Vec<char>> = vec![vec![]; 9];

    lines
        .iter()
        .take_while(|line| !line.is_empty())
        .for_each(|line| {
            for i in 0..crates_count {
                let token: String = line[i * 4..((i + 1) * 4) - 1].into();
                if token.starts_with('[') {
                    stacks[i].insert(0, token.chars().nth(1).unwrap_or_default());
                }
            }
        });

    let mut instructions: Vec<(usize, usize, usize)> = vec![];
    lines
        .iter()
        .filter(|line| line.starts_with("move"))
        .for_each(|line| {
            let tokens: Vec<_> = line.split(' ').collect();
            instructions.push((
                tokens[1].parse().unwrap_or_default(),
                tokens[3].parse().unwrap_or_default(),
                tokens[5].parse().unwrap_or_default(),
            ));
        });

    let mut stacks2 = stacks.clone();
    for (m, f, t) in instructions {
        let idx = stacks[t - 1].len();
        for _ in 0..m {
            let value = stacks[f - 1].pop().unwrap_or_default();
            stacks[t - 1].push(value);

            let value2 = stacks2[f - 1].pop().unwrap_or_default();
            stacks2[t - 1].insert(idx, value2);
        }
    }

    print!("Part 1: ");
    for stack in stacks {
        print!("{}", stack.last().unwrap_or(&'\0'));
    }
    println!();
    print!("Part 2: ");
    for stack in stacks2 {
        print!("{}", stack.last().unwrap_or(&'\0'));
    }

    Ok(())
}
