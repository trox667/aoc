type Button = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | "A" | "B" | "C" | "D";
type Direction = "U" | "L" | "D" | "R";

const neighborMap = new Map<Button, Button[]>();
neighborMap.set(1, [0, 0, 4, 2]);
neighborMap.set(2, [0, 1, 5, 3]);
neighborMap.set(3, [0, 2, 6, 0]);
neighborMap.set(4, [1, 0, 7, 5]);
neighborMap.set(5, [2, 4, 8, 6]);
neighborMap.set(6, [3, 5, 9, 0]);
neighborMap.set(7, [4, 0, 0, 8]);
neighborMap.set(8, [5, 7, 0, 9]);
neighborMap.set(9, [6, 8, 0, 0]);

const neighborMap2 = new Map<Button, Button[]>();
neighborMap2.set(1, [0, 0, 3, 0]);

neighborMap2.set(2, [0, 0, 6, 3]);
neighborMap2.set(3, [1, 2, 7, 4]);
neighborMap2.set(4, [0, 3, 8, 0]);

neighborMap2.set(5, [0, 0, 0, 6]);
neighborMap2.set(6, [2, 5, "A", 7]);
neighborMap2.set(7, [3, 6, "B", 8]);
neighborMap2.set(8, [4, 7, "C", 9]);
neighborMap2.set(9, [0, 8, 0, 0]);

neighborMap2.set("A", [6, 0, 0, "B"]);
neighborMap2.set("B", [7, "A", "D", "C"]);
neighborMap2.set("C", [8, "B", 0, 0]);

neighborMap2.set("D", ["B", 0, 0, 0]);

const getDirectionIndex = (direction: Direction): number | undefined => {
  if (direction === "U") return 0;
  if (direction === "L") return 1;
  if (direction === "D") return 2;
  if (direction === "R") return 3;
  return undefined;
};

class Keypad {
  public button: Button;

  constructor() {
    this.button = 5;
  }

  move(direction: Direction, neighborMap: Map<Button, Button[]>) {
    const neighbors = neighborMap.get(this.button);
    if (!neighbors) return;

    const index = getDirectionIndex(direction);
    if (index === undefined) return;

    const b = neighbors[index];
    if (b !== 0) {
      this.button = b;
    }
  }
}

const run = (lines: string[], neighborMap: Map<Button, Button[]>): string => {
  const keypad = new Keypad();
  const key = lines.map((line) => {
    line.split("").map((d) => d as Direction).forEach((d) =>
      keypad.move(d, neighborMap)
    );
    return keypad.button;
  });
  return key.join("");
};

const TEST = false;

import { assertEquals } from "https://deno.land/std@0.154.0/testing/asserts.ts";

if (TEST) {
  Deno.test("simple sample", () => {
    assertEquals(run(["ULL", "RRDDD", "LURDL", "UUUUD"], neighborMap), "1985");
    assertEquals(run(["ULL", "RRDDD", "LURDL", "UUUUD"], neighborMap2), "5DB3");
  });
} else {
  const input = await Deno.readTextFile("../inputs/input02");
  const lines = input.split("\n").filter((line) => line.length > 0);
  const result1 = run(lines, neighborMap);
  const result2 = run(lines, neighborMap2);

  console.log(`Part 1: ${result1}`);
  console.log(`Part 2: ${result2}`);
}
