use std::cmp::Ordering;

fn main() {
    println!("{}", part1());
}

type Position = (i32, i32);

fn manhattan_distance(position: &Position) -> i32 {
    position.0.abs() + position.1.abs()
}

fn sort_manhattan_distance(position_a: &&Position, position_b: &&Position) -> Ordering {
    manhattan_distance(position_a).cmp(&manhattan_distance(position_b))
}

struct PathData {
    path: std::collections::HashSet<Position>,
    position: Position,
}
impl PathData {
    fn new() -> Self {
        Self {
            path: std::collections::HashSet::new(),
            position: (0, 0),
        }
    }

    fn add(&mut self, x: i32, y: i32) {
        let (cx, cy) = self.position;
        for dx in 0..x.abs() {
            if x < 0 {
                self.path.insert((cx - dx, cy + y));
            } else {
                self.path.insert((cx + dx, cy + y));
            }
        }
        for dy in 0..y.abs() {
            if y < 0 {
                self.path.insert((cx + x, cy - dy));
            } else {
                self.path.insert((cx + x, cy + dy));
            }
        }
        self.position = (self.position.0 + x, self.position.1 + y);
    }
}

fn element_path(data: &mut PathData, element: &str) {
    if let Ok(count) = element[1..].parse::<i32>() {
        match &element[0..1] {
            "U" => {
                data.add(0, count);
            }
            "D" => {
                data.add(0, -count);
            }
            "L" => {
                data.add(-count, 0);
            }
            "R" => {
                data.add(count, 0);
            }
            _ => {}
        }
    }
}

fn trace_path(path: &str) -> PathData {
    let mut data = PathData::new();
    path.split(',').for_each(|n| element_path(&mut data, n));
    data
}

fn run(path: &Vec<&str>) -> i32 {
    let paths_data: Vec<PathData> = path.iter().map(|p| trace_path(p)).collect::<_>();
    if paths_data.len() < 2 {
        0
    } else {
        let a = &paths_data[0];
        let b = &paths_data[1];
        let mut intersection = a
            .path
            .intersection(&b.path)
            .filter(|p| manhattan_distance(p) > 0)
            .collect::<Vec<&Position>>();
        intersection.sort_by(sort_manhattan_distance);
        manhattan_distance(&intersection.get(0).unwrap_or(&&(0, 0)))
    }
}

fn read_input() -> Vec<&'static str> {
    include_str!("../input03").split('\n').collect::<Vec<_>>()
}

fn part1() -> i32 {
    run(&read_input())
}

mod tests {
    use super::*;

    #[test]
    fn test_element_path() {
        let mut data = PathData::new();
        element_path(&mut data, "L8");
        assert_eq!(data.position.0, -8);
        assert_eq!(data.position.1, 0);
        assert_eq!(data.path.len(), 8);
        for x in 0..-8 {
            assert!(data.path.get(&(x, 0)).is_some());
        }

        let mut data = PathData::new();
        element_path(&mut data, "R8");
        assert_eq!(data.position.0, 8);
        assert_eq!(data.position.1, 0);
        assert_eq!(data.path.len(), 8);
        for x in 0..8 {
            assert!(data.path.get(&(x, 0)).is_some());
        }

        let mut data = PathData::new();
        element_path(&mut data, "U8");
        assert_eq!(data.position.0, 0);
        assert_eq!(data.position.1, 8);
        assert_eq!(data.path.len(), 8);
        for y in 0..8 {
            assert!(data.path.get(&(0, y)).is_some());
        }

        let mut data = PathData::new();
        element_path(&mut data, "D8");
        assert_eq!(data.position.0, 0);
        assert_eq!(data.position.1, -8);
        assert_eq!(data.path.len(), 8);
        for y in 0..8 {
            assert!(data.path.get(&(0, -y)).is_some());
        }
    }

    #[test]
    fn test_single_path() {
        let path = "R8,U5,L5,D3";
        let data = trace_path(path);
        assert_eq!(data.path.len(), 21);
        assert_eq!(data.position, (3, 2));
    }

    #[test]
    fn test_run() {
        let paths = vec![
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83",
        ];
        assert_eq!(run(&paths), 159);

        let paths = vec![
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        ];
        assert_eq!(run(&paths), 135);
    }
}
