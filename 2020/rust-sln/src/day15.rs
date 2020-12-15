use fnv::FnvHashMap;

fn main() {
    println!("Part1 {}", part1());
    println!("Part2 {}", part2());
}

fn read_input() -> Vec<usize> {
    vec![14, 1, 17, 0, 3, 20]
}

fn run(inputs: &Vec<usize>, n: usize) -> usize {
    let mut turn = 1;
    let mut memory: FnvHashMap<usize, (usize, usize)> = FnvHashMap::default();
    for i in inputs {
        memory.insert(*i, (turn, 0));
        turn += 1;
    }

    let mut last = *inputs.last().expect("there must be given input");
    while turn <= n {
        if let Some((pre, prepre)) = &memory.get(&last) {
            if *prepre != 0 {
                last = pre - prepre;
            } else {
                last = 0;
            }
        } else {
            memory.insert(last, (turn, 0));
        }

        let pre = match memory.get(&last) {
            Some((p, _)) => *p,
            None => 0,
        };
        memory.insert(last, (turn, pre));
        turn += 1;
    }

    last
}

fn part1() -> usize {
    run(&read_input(), 2020)
}

fn part2() -> usize {
    run(&read_input(), 30_000_000)
}

mod tests {
    use super::*;

    #[test]
    fn test_() {}
}
