const values = new Map<string, { low?: number; high?: number }>();
const dealer = new Map<string, Function>();
const outputs = new Map<string, { low?: number; high?: number }>();

function addChip(target: string, chip: number) {
  const chips = target.startsWith("output")
    ? outputs.get(target) ?? {}
    : values.get(target) ?? {};

  if (chips.low !== undefined) {
    if (chips.low < chip) {
      chips.high = chip;
    } else {
      chips.high = chips.low;
      chips.low = chip;
    }
  } else {
    chips.low = chip;
  }

  if (target.startsWith("output")) {
    outputs.set(target, chips);
  } else {
    values.set(target, chips);
  }
}

function addInstruction(source: string, targetLow: string, targetHigh: string) {
  const instruction = () => {
    const chips = source.startsWith("output")
      ? outputs.get(source)
      : values.get(source);

    if (chips && chips.low && chips.high) {
      addChip(targetLow, chips.low);
      addChip(targetHigh, chips.high);

      if (source.startsWith("output")) {
        outputs.delete(source);
      } else {
        values.delete(source);
      }
    }
  };
  dealer.set(source, instruction);
}

function parseInstruction(instruction: string) {
  const tokens = instruction.split(" ");
  if (instruction.startsWith("value")) {
    const value = parseInt(tokens[1]);
    const target = tokens[4] + " " + tokens[5];

    addChip(target, value);
  } else {
    const source = tokens[0] + " " + tokens[1];
    const low = tokens[5] + " " + tokens[6];
    const high = tokens[10] + " " + tokens[11];
    addInstruction(source, low, high);
  }
}

const input = await Deno.readTextFile("../inputs/input10");
input.split("\n").filter((line) => line.length > 0).map((
  line,
) => parseInstruction(line));

while (values.size > 0) {
  for (const [key, { low, high }] of values.entries()) {
    if (low && high) {
      if (low === 17 && high === 61) {
        console.log("Part 1", key);
      }
      const instruction = dealer.get(key);
      if (instruction) {
        instruction();
      }
    }
  }
}

let result = 1;
for (const [key, { low, high: _high }] of outputs) {
  if (key === "output 1" || key === "output 2" || key === "output 0") {
    result *= low ?? 1;
  }
}

console.log("Part 2", result);
