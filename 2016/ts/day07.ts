const abba = (input: string): boolean => {
  for (let idx = 1; idx < input.length - 2; ++idx) {
    const charA = input.charAt(idx - 1);
    const charB = input.charAt(idx);

    if (charA === charB) continue;

    const test = charA + charB;
    const reverseTest = test.split("").reverse().join("");
    const test2 = input.charAt(idx + 1) + input.charAt(idx + 2);

    if (test2 === reverseTest) {
      return true;
    }
  }

  return false;
};

const aba = (input: string): string[] => {
  const results = [];
  for (let idx = 1; idx < input.length - 1; ++idx) {
    const charA = input.charAt(idx - 1);
    const charB = input.charAt(idx);

    if (charA === charB) continue;

    const test = charB + charA;
    const test2 = charB + input.charAt(idx + 1);
    if (test === test2) {
      results.push(charA + charB + charA);
    }
  }
  return results;
};

const invertAba = (key: string): string =>
  key.charAt(1) + key.charAt(0) + key.charAt(1);

const bab = (input: string, key: string): boolean => input.indexOf(key) !== -1;

enum IPPart {
  HypernetSequence,
  Default,
}

type Tokens = [IPPart, string];

const splitIP = (input: string): Tokens[] => {
  const tokens: Tokens[] = [];

  let value = "";
  let state = IPPart.Default;
  for (const c of input) {
    if (c === "[") {
      tokens.push([state, value.trim()]);
      value = "";
      state = IPPart.HypernetSequence;
    } else if (c === "]") {
      tokens.push([state, value.trim()]);
      value = "";
      state = IPPart.Default;
    } else {
      value += c;
    }
  }
  if (value.length > 0) {
    tokens.push([state, value.trim()]);
  }

  return tokens;
};

const verifyIP = (tokens: Tokens[]): boolean => {
  let partIsAbba = false;
  for (const [part, value] of tokens) {
    const isAbba = abba(value);
    if (part === IPPart.HypernetSequence && isAbba) {
      return false;
    }
    if (part === IPPart.Default && isAbba) {
      partIsAbba = true;
    }
  }

  return partIsAbba;
};

const verifySSL = (tokens: Tokens[]): boolean => {
  const partsAba = tokens.filter(([part, _value]) => part === IPPart.Default)
    .map((
      [_p, value],
    ) => aba(value)).flat(1);

  const hypernetSequences = tokens.filter(([part, _value]) =>
    part === IPPart.HypernetSequence
  );

  for (const aba of partsAba) {
    const babValue = invertAba(aba);
    const countMatches = hypernetSequences.filter(([_p, value]) =>
      bab(value, babValue)
    ).length;
    if (countMatches > 0) return true;
  }

  return false;
};

const input = await Deno.readTextFile("../inputs/input07");

const data = input.split("\n").filter((line) => line.length > 0).map((line) =>
  splitIP(line)
);

// const data2 = `aba[bab]xyz
// xyx[xyx]xyx
// aaa[kek]eke
// zazbz[bzb]cdb`.split("\n").filter((line) => line.length > 0).map((line) =>
//   splitIP(line)
// );
console.log(`Part 1: ${data.filter((tokens) => verifyIP(tokens)).length}`);
console.log(`Part 2: ${data.filter((tokens) => verifySSL(tokens)).length}`);
