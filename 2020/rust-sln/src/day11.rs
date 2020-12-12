fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

type Grid = Vec<Vec<char>>;
type Position = (isize, isize);

fn parse(lines: &str) -> Grid {
    lines
        .split('\n')
        .map(|line| line.trim().chars().collect())
        .collect()
}

fn draw(grid: Grid) {
    for y in 0..grid.len() {
        for x in 0..grid[y].len() {
            print!("{}", grid[y][x]);
        }
        print!("\n");
    }
}

fn make_empty_grid(old_grid: &Grid) -> Grid {
    let height = old_grid.len();
    let width = old_grid[0].len();
    let mut grid = vec![];
    for _ in 0..height {
        let mut grid_row = vec![];
        for _ in 0..width {
            grid_row.push('.');
        }
        grid.push(grid_row);
    }
    grid
}

fn sum_char_in_grid(grid: &Grid, c: char) -> isize {
    let mut count = 0;
    for y in 0..grid.len() {
        for x in 0..grid[y].len() {
            if c == grid[y][x] {
                count += 1;
            }
        }
    }
    count
}

fn read_input() -> &'static str {
    include_str!("../../inputs/input11")
}

fn adjacent_seats(grid: &Grid, position: Position, infinite: bool) -> isize {
    let mut count = 0;
    let directions = vec![
        (-1, 1),
        (0, 1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ];
    let (px, py) = position;
    for direction in directions {
        let (x, y) = direction;
        let mut scale = 1;
        let mut check_position = (px + x * scale, py + y * scale);
        while grid.get(check_position.1 as usize).is_some()
            && grid[check_position.1 as usize]
                .get(check_position.0 as usize)
                .is_some()
        {
            match grid[check_position.1 as usize][check_position.0 as usize] {
                '#' => {
                    count += 1;
                    break;
                }
                'L' => {
                    break;
                }
                _ => {}
            };

            if infinite {
                scale += 1;
                check_position = (px + x * scale, py + y * scale);
            } else {
                break;
            }
        }
    }
    count
}

fn neighbors(grid: &Grid, position: Position) -> isize {
    adjacent_seats(grid, position, false)
}

fn in_sight(grid: &Grid, position: Position) -> isize {
    adjacent_seats(grid, position, true)
}

fn write_to_grid(grid: &mut Grid, position: Position, value: char) {
    grid[position.1 as usize][position.0 as usize] = value;
}

fn get_from_grid(grid: &Grid, position: Position) -> char {
    grid[position.1 as usize][position.0 as usize]
}

fn apply_rules(
    grid: &Grid,
    new_grid: &mut Grid,
    position: Position,
    direct: bool,
    max_adjacent_seats: isize,
) {
    let nc = if direct {
        neighbors(grid, position)
    } else {
        in_sight(grid, position)
    };
    let seat = get_from_grid(grid, position);
    match seat {
        s if s == 'L' && nc == 0 => write_to_grid(new_grid, position, '#'),
        s if s == '#' && nc >= max_adjacent_seats => write_to_grid(new_grid, position, 'L'),
        _ => write_to_grid(new_grid, position, seat),
    };
}

fn turn(grid: &Grid, direct: bool, max_adjacent_seats: isize) -> Grid {
    let mut new_grid = make_empty_grid(grid);
    for y in 0..grid.len() {
        for x in 0..grid[y].len() {
            apply_rules(
                grid,
                &mut new_grid,
                (x as isize, y as isize),
                direct,
                max_adjacent_seats,
            );
        }
    }
    new_grid
}

fn run(input: &str, direct: bool, max_adjacent_seats: isize) -> isize {
    let mut grid = parse(input);
    loop {
        let new_grid = turn(&grid, direct, max_adjacent_seats);
        if new_grid == grid {
            return sum_char_in_grid(&new_grid, '#');
        } else {
            grid = new_grid;
        }
    }
}

fn part1() -> isize {
    run(read_input(), true, 4)
}

fn part2() -> isize {
    run(read_input(), false, 5)
}

mod tests {
    use super::*;

    fn test_input() -> &'static str {
        r#"L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"#
    }
    #[test]
    fn test_parse() {
        let data = parse(test_input());
        assert_eq!(data.len(), 10);
        assert_eq!(data[0].len(), 10);
    }

    #[test]
    fn test_neighbors() {
        let grid = parse(
            r#"###
#.#
###"#,
        );
        assert_eq!(neighbors(&grid, (1, 1)), 8);
        let grid = parse(
            r#"#.#
#.#
.#."#,
        );
        assert_eq!(neighbors(&grid, (1, 1)), 5);
    }
}
