import { permutator, readLines } from "./utils.ts";

type Route = { from: string; to: string; distance: number };

function parse(line: string): Route {
  const tokens = line.split(" ");
  return { from: tokens[0], to: tokens[2], distance: parseInt(tokens[4]) };
}

function addKeys(keys: Set<string>, route: Route) {
  keys.add(route.from);
  keys.add(route.to);
}

function addWeights(weights: Map<string, number>, route: Route) {
  weights.set(`${route.from}:${route.to}`, route.distance);
  weights.set(`${route.to}:${route.from}`, route.distance);
}

function findShortest(keys: Set<string>, weights: Map<string, number>): number {
  const perms = permutator(Array.from(keys));
  let shortest = Number.MAX_SAFE_INTEGER;
  for (const p of perms) {
    let distance = 0;
    for (let i = 0; i < p.length - 1; ++i) {
      const key = `${p[i]}:${p[i + 1]}`;
      distance += weights.get(key) ?? 0;
    }
    shortest = Math.min(distance, shortest);
  }
  return shortest;
}

function findLongest(keys: Set<string>, weights: Map<string, number>): number {
  const perms = permutator(Array.from(keys));
  let longest = 0;
  for (const p of perms) {
    let distance = 0;
    for (let i = 0; i < p.length - 1; ++i) {
      const key = `${p[i]}:${p[i + 1]}`;
      distance += weights.get(key) ?? 0;
    }
    longest = Math.max(distance, longest);
  }
  return longest;
}

function part1() {
  const keys = new Set<string>();
  const weights = new Map<string, number>();
  const routes = readLines("../inputs/input09").filter((line) =>
    line.length > 0
  ).map((line) => parse(line));
  routes.forEach((route) => {
    addKeys(keys, route);
    addWeights(weights, route);
  });
  const part1 = findShortest(keys, weights);
  console.log(`Part 1: ${part1}`);
}

part1();

function part2() {
  const keys = new Set<string>();
  const weights = new Map<string, number>();
  const routes = readLines("../inputs/input09").filter((line) =>
    line.length > 0
  ).map((line) => parse(line));
  routes.forEach((route) => {
    addKeys(keys, route);
    addWeights(weights, route);
  });
  const part2 = findLongest(keys, weights);
  console.log(`Part 2: ${part2}`);
}

part2();
