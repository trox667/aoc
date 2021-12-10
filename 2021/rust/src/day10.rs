enum ParserOutput {
    Error(char),
    Added(Vec<char>),
}

fn is_opening(c: char) -> bool {
    "([{<".contains(c)
}

fn is_closing(c: char) -> bool {
    ")]}>".contains(c)
}

fn get_closing(c: char) -> Option<char> {
    match c {
        '(' => Some(')'),
        '[' => Some(']'),
        '{' => Some('}'),
        '<' => Some('>'),
        _ => None,
    }
}

fn get_opening(c: char) -> Option<char> {
    match c {
        ')' => Some('('),
        ']' => Some('['),
        '}' => Some('{'),
        '>' => Some('<'),
        _ => None,
    }
}

fn points1(c: char) -> usize {
    match c {
        ')' => 3,
        ']' => 57,
        '}' => 1197,
        '>' => 25137,
        _ => 0,
    }
}

fn points2(c: char) -> usize {
    match c {
        ')' => 1,
        ']' => 2,
        '}' => 3,
        '>' => 4,
        _ => 0,
    }
}

fn parse(chunk: &str) -> ParserOutput {
    let mut stack = vec![];
    let mut i = 0;
    let mut error = false;
    for c in chunk.chars() {
        if is_opening(c) {
            stack.push(c);
        } else if is_closing(c) {
            if !stack.is_empty() && get_opening(c).unwrap() == *stack.last().unwrap() {
                stack.pop().unwrap();
            } else {
                error = true;
            }
        }
        if !error {
            i += 1;
        }
    }

    if !error {
        let mut added = vec![];
        stack.reverse();
        for s in stack {
            added.push(get_closing(s).unwrap());
        }
        ParserOutput::Added(added)
    } else {
        ParserOutput::Error(chunk.chars().nth(i).unwrap())
    }
}

pub fn part1(lines: &Vec<String>) -> usize {
    let mut sum = 0;
    for line in lines {
        sum += match parse(line) {
            ParserOutput::Error(c) => points1(c),
            _ => 0,
        };
    }
    sum
}

pub fn part2(lines: &Vec<String>) -> usize {
    let mut results = vec![];
    for line in lines {
        match parse(line) {
            ParserOutput::Added(added) => {
                let mut points = 0;
                for a in added {
                    points *= 5;
                    points += points2(a);
                }
                if points > 0 {
                    results.push(points);
                }
            }
            _ => {}
        };
    }
    results.sort();
    results[results.len() / 2]
}
