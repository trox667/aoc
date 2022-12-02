use anyhow::Result;
use std::fs;

static DRAW: usize = 3;
static WIN: usize = 6;

fn to_number(token: &str) -> usize {
    match token {
        "A" | "X" => 1,
        "B" | "Y" => 2,
        "C" | "Z" => 3,
        _ => 0,
    }
}

fn play1(opponent: usize, player: usize) -> usize {
    return if opponent == player {
        DRAW + player
    } else if (opponent + 1) == player || opponent == 3 && player == 1 {
        WIN + player
    } else {
        player
    };
}

fn play2(opponent: usize, action: usize) -> usize {
    return if action == 2 {
        DRAW + opponent
    } else if action == 1 {
        if opponent == 1 {
            3
        } else {
            opponent - 1
        }
    } else {
        if opponent == 3 {
            1 + WIN
        } else {
            opponent + 1 + WIN
        }
    };
}

fn play_round(play: fn(usize, usize) -> usize) -> Result<usize> {
    return Ok(fs::read_to_string("../inputs/input2")?
        .split("\n")
        .filter_map(|line| {
            if line.is_empty() {
                return None;
            }
            let tokens: Vec<usize> = line
                .split(" ")
                .take(2)
                .map(|token| to_number(token))
                .collect();
            Some(tokens)
        })
        .map(|values| play(values[0], values[1]))
        .sum());
}

fn main() -> Result<()> {
    let part1: usize = play_round(play1)?;
    println!("Part 1: {part1}");
    let part2: usize = play_round(play2)?;
    println!("Part 2: {part2}");
    Ok(())
}
