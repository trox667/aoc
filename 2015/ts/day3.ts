import { readLines } from "./utils.ts";

type Coordinate = { x: number; y: number };

function toString(coordinate: Coordinate): string {
  return `${coordinate.x},${coordinate.y}`;
}

const Directions: Map<string, Coordinate> = new Map([
  ["<", { x: -1, y: 0 }],
  ["^", { x: 0, y: 1 }],
  [">", { x: 1, y: 0 }],
  ["v", { x: 0, y: -1 }],
]);

export function parse(lines: string[]): Coordinate[][] {
  return lines.map((line) =>
    line.split("").map((token) => {
      const coordinate = Directions.get(token);
      if (!coordinate) {
        Deno.exit(-1);
      }
      return coordinate;
    })
  );
}

export function walk(coordinates: Coordinate[]): number {
  const currentCoordinate: Coordinate = { x: 0, y: 0 };
  const visited = new Set();
  visited.add(toString(currentCoordinate));

  coordinates.forEach((coordinate) => {
    currentCoordinate.x += coordinate.x;
    currentCoordinate.y += coordinate.y;

    visited.add(toString(currentCoordinate));
  });
  return visited.size;
}

export function walk2(coordinates: Coordinate[]): number {
  const currentCoordinateSanta: Coordinate = { x: 0, y: 0 };
  const currentCoordinateSantaRobot: Coordinate = { x: 0, y: 0 };

  const visited = new Set();

  visited.add(toString(currentCoordinateSanta));

  for (let i = 0; i < coordinates.length; ++i) {
    const coordinate = coordinates[i];
    if (i % 2 !== 0) {
      currentCoordinateSanta.x += coordinate.x;
      currentCoordinateSanta.y += coordinate.y;
      visited.add(toString(currentCoordinateSanta));
    } else {
      currentCoordinateSantaRobot.x += coordinate.x;
      currentCoordinateSantaRobot.y += coordinate.y;
      visited.add(toString(currentCoordinateSantaRobot));
    }
  }

  return visited.size;
}

export function part1() {
  parse(readLines("../inputs/input03")).map((coordinates) => walk(coordinates))
    .forEach((value) => console.log(`Part1: ${value}`));
}

export function part2() {
  parse(readLines("../inputs/input03")).map((coordinates) => walk2(coordinates))
    .forEach((value) => console.log(`Part2: ${value}`));
}

part1();
part2();
