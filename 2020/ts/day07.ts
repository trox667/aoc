import * as fs from "fs";

type Bag = [string, Map<string, number>];

export function read_input(): Array<Bag> {
  return fs
    .readFileSync("../inputs/input07", "utf8")
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line.length > 0)
    .map((line) => parse(line));
}

function get_range(s: number, e: number, line: string) {
  return line
    .split(" ")
    .filter((_: string, i: number) => i >= s && i < e)
    .join(" ");
}

function parse(line: string): Bag {
  const bag = get_range(0, 2, line);
  const second = line.split(" contain ")[1];
  if (line.indexOf(" no other ") != -1) {
    return [bag, new Map()];
  } else if (line.indexOf(", ") != -1) {
    const tokens = second.split(", ").map((token) => token.replace(".", ""));
    const depsMap = new Map<string, number>();
    tokens.forEach((token) => {
      depsMap.set(get_range(1, 3, token), parseInt(token[0]));
    });
    return [bag, depsMap];
  } else {
    const count = parseInt(second.split(" ")[0]);
    const dep = get_range(1, 3, second);
    const depsMap = new Map<string, number>();
    depsMap.set(dep, count);
    return [bag, depsMap];
  }
}

function part1() {
  const bags = read_input();
  let queue = ["shiny gold"];
  const matching_bags = new Set<string>();

  while (queue.length > 0) {
    const search_bag = queue.shift();
    for (const bag of bags) {
      bag[1].forEach((_, name) => {
        if (name == search_bag) {
          queue.push(bag[0]);
          matching_bags.add(bag[0]);
        }
      });
    }
  }
  console.log(matching_bags.size);
}

function getBag(name: string, bags: Array<Bag>): Bag {
  for (const bag of bags) {
    if (bag[0] == name) return bag;
  }

  return null;
}

function countDeps(bag: Bag, bags: Array<Bag>): number {
  if (bag[1].size == 0) return 0;
  let count = 0;
  bag[1].forEach((v, name) => {
    const b = getBag(name, bags);
    count += v + v * countDeps(b, bags);
  });
  return count;
}

function part2() {
  const bags = read_input();
  const shinyBag = getBag("shiny gold", bags);
  console.log(countDeps(shinyBag, bags));
}

part1();
part2();
