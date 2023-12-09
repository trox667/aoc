// const input = await Deno.readTextFile("../input/sample09");
const input = await Deno.readTextFile("../input/input09");

const differences = (history: number[]): number[] => {
  const diffs = [];
  for (let i = 1; i < history.length; i++) {
    diffs.push(history[i] - history[i - 1]);
  }
  return diffs;
};

const isZero = (history: number[]): boolean => history.every((n) => n === 0);

let part1 = 0;
let part2 = 0;
for (const line of input.split("\n").filter((l) => l.length)) {
  const history = line.split(" ").map((n) => parseInt(n));
  let current = [...history];
  let steps = [history];
  while (!isZero(current)) {
    current = differences(current);
    steps.push(current);
  }
  steps.pop();
  steps = steps.reverse();
  let lastPart1Value = 0;
  let lastPart2Value = 0;
  for (const step of steps) {
    lastPart1Value = step[step.length - 1] + lastPart1Value;
    lastPart2Value = step[0] - lastPart2Value;
  }
  part1 += lastPart1Value;
  part2 += lastPart2Value;
}

console.log("Part 1:", part1);
console.log("Part 2:", part2);
