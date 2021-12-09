use std::collections::HashSet;

fn create_heightmap(lines: &Vec<String>) -> Vec<i32> {
    lines
        .iter()
        .flat_map(|s| {
            s.chars()
                .map(|c| c.to_digit(10).unwrap() as i32)
                .collect::<Vec<_>>()
        })
        .collect()
}

fn index(x: i32, y: i32, width: i32) -> i32 {
    y * width + x
}

fn position(idx: i32, width: i32) -> (i32, i32) {
    (idx % width, idx / width)
}

fn get_neighbors(x: i32, y: i32, width: i32, height: i32) -> Vec<i32> {
    let mut neighbors = vec![];
    if x - 1 >= 0 {
        neighbors.push(index(x - 1, y, width));
    }
    if x + 1 < width {
        neighbors.push(index(x + 1, y, width));
    }
    if y - 1 >= 0 {
        neighbors.push(index(x, y - 1, width));
    }
    if y + 1 < height {
        neighbors.push(index(x, y + 1, width));
    }
    neighbors
}

fn get_low_points(heightmap: &Vec<i32>, width: i32, height: i32) -> HashSet<i32> {
    let mut low_points = HashSet::<i32>::new();
    for i in 0..heightmap.len() {
        let (x, y) = position(i as i32, width);
        let curr_height = heightmap[i];
        if curr_height == 9 {
            continue;
        }

        let neighbors = get_neighbors(x, y, width, height);
        if curr_height
            < neighbors
                .iter()
                .map(|n| heightmap[*n as usize])
                .min()
                .unwrap()
        {
            low_points.insert(i as i32);
        }
    }
    low_points
}

fn get_basin(
    idx: i32,
    heightmap: &Vec<i32>,
    width: i32,
    height: i32,
    basin: &mut HashSet<i32>,
    visited: &mut HashSet<i32>,
) {
    visited.insert(idx);
    let (x, y) = position(idx as i32, width);
    let curr_height = heightmap[idx as usize];
    if curr_height == 9 {
        return;
    }
    basin.insert(idx);
    let neighbors = get_neighbors(x, y, width, height);
    for neighbor in neighbors {
        if !visited.contains(&neighbor) && heightmap[neighbor as usize] != 9 {
            get_basin(neighbor, heightmap, width, height, basin, visited);
        }
    }
}

pub fn part1(lines: &Vec<String>) -> i32 {
    let width = lines[0].len();
    let height = lines.len();
    let heightmap = create_heightmap(lines);
    let low_points = get_low_points(&heightmap, width as i32, height as i32);
    let r = low_points
        .iter()
        .map(|lp| heightmap[*lp as usize] + 1)
        .sum::<i32>();
    r as i32
}

pub fn part2(lines: &Vec<String>) -> i32 {
    let width = lines[0].len();
    let height = lines.len();
    let heightmap = create_heightmap(lines);

    let mut results = vec![];
    let mut visited = HashSet::<i32>::new();
    for idx in get_low_points(&heightmap, width as i32, height as i32) {
        let mut basin = HashSet::<i32>::new();
        get_basin(
            idx,
            &heightmap,
            width as i32,
            height as i32,
            &mut basin,
            &mut visited,
        );
        results.push(basin);
    }
    results.sort_by(|a, b| a.len().partial_cmp(&b.len()).unwrap());
    results.reverse();
    results
        .iter()
        .take(3)
        .map(|a| a.len() as i32)
        .reduce(|a, b| a * b)
        .unwrap()
}
