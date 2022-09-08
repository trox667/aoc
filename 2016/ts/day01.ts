enum Direction {
  "L",
  "R",
}

type Instruction = {
  direction: Direction;
  distance: number;
};

const parseInstruction = (str: string): Instruction | undefined => {
  const tokens = str.match(/(?<direction>L|R)(?<distance>[0-9]*)/);

  if (tokens && tokens.length >= 3) {
    return {
      direction: Direction[tokens[1] as keyof typeof Direction],
      distance: parseInt(tokens[2]),
    };
  } else {
    return undefined;
  }
};

enum Orientation {
  North,
  East,
  South,
  West,
}

class Position {
  constructor(public x = 0, public y = 0) {}
  toString(): string {
    return `(${this.x},${this.y})`;
  }
  add(pos: Position) {
    this.x += pos.x;
    this.y += pos.y;
  }
}

const defaultPosition = (): Position => new Position();
const orientationMap = new Map<string, [Orientation, Position]>();
orientationMap.set(`${Orientation.North}:${Direction.L}`, [
  Orientation.West,
  new Position(-1, 0),
]);
orientationMap.set(`${Orientation.North}:${Direction.R}`, [
  Orientation.East,
  new Position(1, 0),
]);
orientationMap.set(`${Orientation.East}:${Direction.L}`, [
  Orientation.North,
  new Position(0, 1),
]);
orientationMap.set(`${Orientation.East}:${Direction.R}`, [
  Orientation.South,
  new Position(0, -1),
]);
orientationMap.set(`${Orientation.South}:${Direction.L}`, [
  Orientation.East,
  new Position(1, 0),
]);
orientationMap.set(`${Orientation.South}:${Direction.R}`, [
  Orientation.West,
  new Position(-1, 0),
]);
orientationMap.set(`${Orientation.West}:${Direction.L}`, [
  Orientation.South,
  new Position(0, -1),
]);
orientationMap.set(`${Orientation.West}:${Direction.R}`, [
  Orientation.North,
  new Position(0, 1),
]);

const manhattanDistance = (a: Position, b: Position): number =>
  Math.abs(a.x - b.x) + Math.abs(a.y - b.y);

class Path {
  private position: Position;
  private orientation: Orientation;
  private trace: Set<string>;
  private easterBunnyHQ: Position | undefined;

  constructor() {
    this.position = defaultPosition();
    this.orientation = Orientation.North;
    this.trace = new Set();
    this.trace.add(new Position().toString());
    this.easterBunnyHQ = undefined;
  }

  getDistance(): number {
    return manhattanDistance(this.position, defaultPosition());
  }

  getHqDistance(): number {
    if (this.easterBunnyHQ) {
      return manhattanDistance(this.easterBunnyHQ, defaultPosition());
    } else {
      return 0;
    }
  }

  private tracePosition(position: Position) {
    if (this.trace.has(position.toString()) && !this.easterBunnyHQ) {
      this.easterBunnyHQ = new Position(position.x, position.y);
    }
    this.trace.add(position.toString());
  }

  walk(instruction: Instruction) {
    const key = `${this.orientation}:${instruction.direction}`;
    const value = orientationMap.get(key);
    if (value) {
      const orientation = value[0];
      const offset = value[1];
      for (let i = 0; i < instruction.distance; ++i) {
        this.position.add(offset);
        this.tracePosition(this.position);
      }
      this.orientation = orientation;
    }
  }
}

const run = (str: string): [number, number] => {
  const path = new Path();

  str.split(",").map((t) => parseInstruction(t.trim()))
    .filter((i): i is Instruction => i !== undefined).forEach((i) =>
      path.walk(i)
    );

  return [path.getDistance(), path.getHqDistance()];
};
const input = await Deno.readTextFile("../inputs/input01");
const result = run(input);
console.log(`Part1: ${result[0]}`);
console.log(`Part2: ${result[1]}`);
