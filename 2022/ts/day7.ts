import { assert } from "./deps.ts";
import { readLines } from "./utils.ts";

export class File {
  constructor(public name: string, public size: number) {}
}
export class Directory {
  constructor(public name: string, public children: Item[] = []) {}
}
export type Item = Directory | File;

export class Tree {
  constructor(public root: Directory) {}

  private getSize(directory: Directory): number {
    let result = 0;

    for (const child of directory.children) {
      if (child instanceof File) {
        result += child.size;
      } else if (child instanceof Directory) {
        result += this.getSize(child);
      }
    }

    return result;
  }

  size(directory: Directory): number {
    return this.getSize(directory);
  }

  private getDirectories(directory: Directory): Directory[] {
    let result: Directory[] = [];
    for (const child of directory.children) {
      if (child instanceof Directory) {
        result.push(child);
        result = result.concat(this.getDirectories(child));
      }
    }
    return result;
  }

  directories(): Directory[] {
    const result = [this.root];
    return result.concat(this.getDirectories(this.root));
  }

  get(currentDirectory: Directory, name: string): Directory | undefined {
    if (name === this.root.name) {
      return this.root;
    }
    for (const child of currentDirectory.children) {
      if (child instanceof Directory) {
        if (child.name === name) {
          return child;
        }
      }
    }
    return undefined;
  }

  insert(currentDirectory: Directory, addItem: Item) {
    currentDirectory.children.push(addItem);
  }
}

export function parse(lines: string[]): Tree {
  const tree = new Tree(new Directory("/"));
  const currentDirectories: Directory[] = [tree.root];
  for (const line of lines) {
    const tokens = line.split(" ");
    if (line.startsWith("$ cd")) {
      if (tokens[2] === "..") {
        currentDirectories.pop();
        continue;
      }
      const dir = currentDirectories[currentDirectories.length - 1];
      const newDir = tree.get(dir, tokens[2]);
      if (newDir && dir !== newDir) {
        currentDirectories.push(newDir);
      }
    } else if (line.startsWith("dir ")) {
      tree.insert(
        currentDirectories[currentDirectories.length - 1],
        new Directory(tokens[1]),
      );
    } else {
      const size = parseInt(tokens[0]);
      if (Number.isNaN(size)) continue;
      tree.insert(
        currentDirectories[currentDirectories.length - 1],
        new File(tokens[1], size),
      );
    }
  }
  return tree;
}

export function run(lines: string[]): number {
  const tree = parse(lines);
  const directories = tree.directories();
  let result = 0;
  for (const dir of directories) {
    const size = tree.size(dir);
    if (size <= 100000) {
      result += size;
    }
  }
  return result;
}

function part1() {
  const lines = readLines("../inputs/input7").filter((line) => line.length > 0);
  const part1 = run(lines);
  console.log(`Part 1: ${part1}`);
}

part1();

export function run2(lines: string[]): number {
  const tree = parse(lines);
  const target = 30000000 - (70000000 - tree.size(tree.root));
  const directories = tree.directories();
  let result = Number.MAX_VALUE;
  for (const dir of directories) {
    const size = tree.size(dir);
    if (size > target) {
      result = Math.min(size, result);
    }
  }
  return result;
}

function part2() {
  const lines = readLines("../inputs/input7").filter((line) => line.length > 0);
  const part2 = run2(lines);
  console.log(`Part 2: ${part2}`);
}

part2();
