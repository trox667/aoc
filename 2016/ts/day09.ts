const parseInput = (input: string, part2 = false): string => {
  let text = "";
  let value = "";
  let i = 0;
  while (i < input.length) {
    const c = input.charAt(i);

    if (c === "(") {
      text += value;
      value = "";
    } else if (c === ")") {
      const [count, repeat] = value.split("x").map((v) => parseInt(v));

      const remaining = input.substring(i + 1, i + 1 + count);
      if (!part2) {
        for (let j = 0; j < repeat; ++j) {
          text += remaining;
        }
        i += remaining.length;
      } else {
        const temp = parseInput(remaining, true);
        for (let j = 0; j < repeat; ++j) {
          text += temp;
        }
        i += remaining.length;
      }

      value = "";
    } else if (c === " ") {
      continue;
    } else {
      value += c;
    }
    ++i;
  }
  if (value.length > 0) {
    text += value;
  }

  return text;
};

console.log(parseInput("A(1x5)BC").length, 7);
console.log(parseInput("(3x3)XYZ").length, 9);
console.log(parseInput("A(2x2)BCD(2x2)EFG").length, 11);
console.log(parseInput("(6x1)(1x3)A").length, 6);
console.log(parseInput("X(8x2)(3x3)ABCY").length, 18);

const input = await Deno.readTextFile("../inputs/input09");
console.log(
  `Part 1: ${
    parseInput(input.split("\n").filter((line) => line.length > 0).join(""))
      .length
  }`,
);

console.log(parseInput("(3x3)XYZ", true).length, 9);
console.log(parseInput("X(8x2)(3x3)ABCY", true).length, 20);
console.log(
  parseInput("(27x12)(20x12)(13x14)(7x10)(1x12)A", true).length,
  241920,
);
console.log(
  parseInput("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", true)
    .length,
  445,
);
console.log(
  `Part 2: ${
    parseInput(
      input.split("\n").filter((line) => line.length > 0).join(""),
      true,
    )
      .length
  }`,
);
