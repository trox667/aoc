fn positions(lines: &Vec<String>) -> Vec<i32> {
    lines[0].split(",").map(|t| { t.parse::<i32>().unwrap() }).collect()
}

fn run(positions: &Vec<i32>, calc_fuel: &dyn Fn(i32) -> i32) -> i32 {
    let max = positions.iter().max().unwrap();
    let min = positions.iter().min().unwrap();
    let mut min_fuel = i32::MAX;
    for i in *min..=*max {
        let mut fuel = 0;
        for j in positions {
            fuel += calc_fuel((i - j).abs());
        }
        min_fuel = min_fuel.min(fuel);
    }
    min_fuel
}

pub fn part1(lines: &Vec<String>) -> i32 {
    run(&positions(lines), &|d: i32| { d })
}

pub fn part2(lines: &Vec<String>) -> i32 {
    run(&positions(lines), &|d: i32| { (d*d+d)/2 })
}