use std::collections::HashSet;

fn create_energy_level(lines: &Vec<String>) -> Vec<Vec<usize>> {
    lines
        .iter()
        .map(|line| {
            line.chars()
                .map(|c| c.to_digit(10).unwrap() as usize)
                .collect()
        })
        .collect()
}

fn get_neighbors(x: usize, y: usize, width: usize, height: usize) -> Vec<(usize, usize)> {
    let mut neighbors = vec![(x, y + 1), (x + 1, y), (x + 1, y + 1)];
    if x >= 1 {
        neighbors.push((x - 1, y));
        neighbors.push((x - 1, y + 1));
    }
    if x >= 1 && y >= 1 {
        neighbors.push((x - 1, y - 1));
    }
    if y >= 1 {
        neighbors.push((x, y - 1));
        neighbors.push((x + 1, y - 1));
    }
    neighbors
        .into_iter()
        .filter(|n| n.0 < width && n.1 < height)
        .collect()
}

fn update(
    positions: &Vec<(usize, usize)>,
    energy_level: &mut Vec<Vec<usize>>,
    flashed: &HashSet<(usize, usize)>,
) -> Vec<(usize, usize)> {
    let mut flashing = vec![];
    for position in positions {
        if flashed.contains(position) {
            continue;
        }
        let (x, y) = position;
        energy_level[*y][*x] += 1;
        if energy_level[*y][*x] > 9 {
            flashing.push((*x, *y));
            energy_level[*y][*x] = 0;
        }
    }
    flashing
}

fn is_sum_zero(energy_level: &Vec<Vec<usize>>) -> bool {
    let height = energy_level.len();
    let width = energy_level[0].len();
    for y in 0..height {
        for x in 0..width {
            if energy_level[y][x] > 0 {
                return false;
            }
        }
    }
    true
}

fn run(steps: usize, energy_level: &mut Vec<Vec<usize>>) -> usize {
    let height = energy_level.len();
    let width = energy_level[0].len();
    let mut positions = vec![];
    for y in 0..height {
        for x in 0..width {
            positions.push((x, y));
        }
    }
    let mut flash_counter = 0;
    for step in 0..steps {
        if is_sum_zero(&energy_level) {
            return step;
        }
        let mut current_flashes =
            update(&positions, energy_level, &HashSet::<(usize, usize)>::new());

        let mut skip_flashes = HashSet::<(usize, usize)>::from_iter(current_flashes.clone());
        flash_counter += current_flashes.len();
        while !current_flashes.is_empty() {
            let (x, y) = current_flashes.pop().unwrap();
            let mut neighbor_flashes = update(
                &get_neighbors(x, y, width, height),
                energy_level,
                &skip_flashes,
            );
            flash_counter += neighbor_flashes.len();
            skip_flashes.extend(neighbor_flashes.clone());
            current_flashes.append(&mut neighbor_flashes);
        }
    }
    flash_counter
}

pub fn part1(lines: &Vec<String>) -> usize {
    run(100, &mut create_energy_level(lines))
}

pub fn part2(lines: &Vec<String>) -> usize {
    run(1000, &mut create_energy_level(lines))
}
