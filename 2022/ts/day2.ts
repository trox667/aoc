import { readLines } from "./utils.ts";

const WINSCORE = 6;
const DRAWSCORE = 3;

function keyMapping(key: string): number {
  if (key === "A" || key === "X") return 1;
  else if (key === "B" || key === "Y") return 2;
  else if (key === "C" || key === "Z") return 3;
  return 0;
}

export function parse(line: string): [number, number] {
  const hands = line.split(" ").map((token) => keyMapping(token));
  if (hands.length == 2) {
    return [hands[0], hands[1]];
  } else {
    Deno.exit(-1);
  }
}

export function play(hands: [number, number]): number {
  let score = 0;
  const [opponent, player] = hands;
  if (opponent + 1 === player || opponent === 3 && player === 1) {
    score = player + WINSCORE;
  } else if (opponent === player) {
    score = player + DRAWSCORE;
  } else {
    score = player;
  }
  return score;
}

export function play2(hands: [number, number]): number {
  let score = 0;
  const [opponent, player] = hands;

  if (player === 1) {
    score = opponent === 1 ? 3 : opponent - 1;
  } else if (player === 2) {
    score = opponent + DRAWSCORE;
  } else if (player === 3) {
    score = opponent === 3 ? 1 : opponent + 1;
    score += WINSCORE;
  } else {
    Deno.exit(-1);
  }

  return score;
}

export function playRounds(lines: string[], playStyle = play): number {
  return lines.map((line) => playStyle(parse(line))).reduce(
    (acc, value) => acc + value,
    0,
  );
}

function part1() {
  console.log(
    "Part 1: ",
    playRounds(
      readLines("../inputs/input2").filter((line) => line.length > 0),
    ),
  );
}

part1();

function part2() {
  console.log(
    "Part 2: ",
    playRounds(
      readLines("../inputs/input2").filter((line) => line.length > 0),
      play2,
    ),
  );
}

part2();
