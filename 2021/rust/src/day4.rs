type Cell = (i32, bool);
type Grid = Vec<Vec<Cell>>;

struct Board {
    grid: Grid,
    last_value: i32,
    completed: bool,
}

impl Board {
    fn new(grid: Grid) -> Board {
        Board { grid, last_value: 0, completed: false }
    }

    fn mark(&mut self, value: i32) {
        for y in 0..5 {
            for x in 0..5 {
                if self.grid[y][x].0 == value {
                    self.grid[y][x] = (self.grid[y][x].0, true);
                    self.last_value = value;
                }
            }
        }
    }

    fn is_complete(&mut self) -> bool {
        for i in 0..5 {
            if (self.grid[0][i].1 && self.grid[1][i].1 && self.grid[2][i].1 && self.grid[3][i].1 && self.grid[4][i].1) ||
                (self.grid[i][0].1 && self.grid[i][1].1 && self.grid[i][2].1 && self.grid[i][3].1 && self.grid[i][4].1) {
                self.completed = true;
                return true;
            }
        }
        false
    }

    fn sum(&self) -> i32 {
        let mut s = 0;
        for y in 0..5 {
            for x in 0..5 {
                if !self.grid[y][x].1 {
                    s += self.grid[y][x].0;
                }
            }
        }
        s
    }

    fn result(&self) -> i32 {
        self.sum() * self.last_value
    }
}

struct Game<'a> {
    boards: &'a mut Vec<Board>,
}

impl Game<'_> {
    fn new(boards: &mut Vec<Board>) -> Game {
        Game {boards: boards}
    }

    fn run(&mut self, numbers: &Vec<i32>, early_exit: bool) -> i32 {
        let mut results = vec![];
        for number in numbers {
            for board in self.boards.iter_mut() {
                if board.completed {
                    continue;
                }
                board.mark(*number);
                if board.is_complete() {
                    results.push(board.result());
                    if early_exit {
                        return results.pop().unwrap();
                    }
                }
            }
        }
        return results.pop().unwrap();
    }
}

fn create_numbers(line: &str) -> Vec<i32> {
    line.split(',').map(|t| { t.parse::<i32>().unwrap() }).collect()
}

fn create_board(lines: &[String]) -> Grid {
    let mut rows = vec![];
    for line in lines {
        let mut row = vec![];
        for token in line.split_whitespace() {
            row.push((token.parse::<i32>().unwrap(), false));
        }
        rows.push(row);
    }
    rows
}

pub fn part1(lines: &Vec<String>) -> i32 {
    let n = create_numbers(lines.get(0).unwrap());
    let mut boards = vec![];
    let lines = &lines[1..];
    for i in (0..lines.len()).step_by(5) {
        boards.push(Board::new(create_board(&lines[i..i + 5])));
    }
    Game::new(&mut boards).run(&n, true)
}

pub fn part2(lines: &Vec<String>) -> i32 {
    let n = create_numbers(lines.get(0).unwrap());
    let mut boards = vec![];
    let lines = &lines[1..];
    for i in (0..lines.len()).step_by(5) {
        boards.push(Board::new(create_board(&lines[i..i + 5])));
    }
    Game::new(&mut boards).run(&n, false)
}