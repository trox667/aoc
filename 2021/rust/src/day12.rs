use std::collections::HashMap;

struct Graph<'a> {
    graph: HashMap<&'a str, Vec<&'a str>>,
    visited: HashMap<&'a str, isize>,
    current_path: Vec<&'a str>,
    paths: Vec<Vec<&'a str>>,
}

impl<'a> Graph<'a> {
    fn new() -> Self {
        Self {
            graph: HashMap::<&str, Vec<&str>>::new(),
            visited: HashMap::<&str, isize>::new(),
            current_path: vec![],
            paths: vec![],
        }
    }

    fn add_edge(&mut self, a: &'a str, b: &'a str) {
        self.graph.entry(a).or_insert(vec![]);
        self.graph.get_mut(a).unwrap().push(b);
        self.graph.entry(b).or_insert(vec![]);
        self.graph.get_mut(b).unwrap().push(a);
    }

    fn dfs(
        &mut self,
        start: &'a str,
        end: &'a str,
        abort: &dyn Fn(&HashMap<&str, isize>, &str) -> bool,
    ) {
        if abort(&self.visited, start) {
            return;
        }

        if start.chars().all(|c| c.is_lowercase()) {
            *self.visited.entry(start).or_insert(0) += 1;
        }
        self.current_path.push(start);
        if start == end {
            self.paths.push(self.current_path.clone());
            *self.visited.entry(start).or_insert(0) -= 1;
            self.current_path.pop();
            return;
        }
        for neighbor in &self.graph[start].clone() {
            self.dfs(neighbor, end, &abort);
        }
        self.current_path.pop();
        *self.visited.entry(start).or_insert(0) -= 1;
    }

    fn count_paths(&self) -> usize {
        self.paths.len()
    }
}

fn create_graph(lines: &Vec<String>) -> Graph {
    let mut graph = Graph::new();
    for line in lines {
        let tokens = line.split('-').collect::<Vec<&str>>();
        graph.add_edge(tokens[0], tokens[1]);
    }
    graph
}

pub fn part1(lines: &Vec<String>) -> usize {
    let abort = |v: &HashMap<&str, isize>, n: &str| v.contains_key(n) && v[n] == 1;
    let mut graph = create_graph(lines);
    graph.dfs("start", "end", &abort);
    graph.count_paths()
}

pub fn part2(lines: &Vec<String>) -> usize {
    let abort = |v: &HashMap<&str, isize>, n: &str| {
        let visited_twice = v.values().any(|v| *v >= 2);
        if visited_twice && v.contains_key(n) && v[n] >= 1 {
            return true;
        } else if (n == "start" || n == "end") && v.contains_key(n) && v[n] >= 1 {
            return true;
        }
        false
    };
    let mut graph = create_graph(lines);
    graph.dfs("start", "end", &abort);
    graph.count_paths()
}
