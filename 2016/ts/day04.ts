import { assertEquals } from "https://deno.land/std@0.154.0/testing/asserts.ts";
const isNumber = (c: string): boolean => {
  try {
    const n = parseInt(c);
    if (Number.isNaN(n) || n === undefined) {
      return false;
    }
    return true;
  } catch {
    return false;
  }
};

const name = (line: string, removeDash = true) => {
  const result = [];
  for (const c of line) {
    if (isNumber(c) || c === "[" || c === "]") {
      return result.join("").replaceAll(removeDash ? "-" : "", "");
    } else {
      result.push(c);
    }
  }
  return result.join("").replaceAll("-", "");
};

const digit = (line: string) => {
  const match = line.match(/(\d+)/);
  if (match) {
    return parseInt(match[0]);
  } else {
    return 0;
  }
};

const checksum = (line: string) => {
  const match = line.match(/(\[[A-z]*\])/);
  if (match) {
    return match[0].replace("[", "").replace("]", "");
  } else {
    return "";
  }
};

const countLetter = (line: string, letter: string): number =>
  line.split("").filter((l) => l === letter).length;

type LetterCount = [string, number];

const countAndSort = (name: string): LetterCount[] => {
  const result: LetterCount[] = [];
  const letters = new Set(name);
  for (const letter of letters) {
    const count = countLetter(name, letter);
    result.push([letter, count]);
  }
  result.sort((a: LetterCount, b: LetterCount) => {
    const [al, ac] = a;
    const [bl, bc] = b;
    if (ac === bc) {
      if (al > bl) return 1;
      else if (al < bl) return -1;
      else return 0;
    }

    return bc - ac;
  });
  return result;
};

const validateChecksum = (letterCount: LetterCount[], checksum: string) => {
  for (let i = 0; i < checksum.length; ++i) {
    if (checksum.charAt(i) !== letterCount[i][0]) {
      return false;
    }
  }
  return true;
};

const decrypt = (name: string, shift: number): string => {
  const result = [];
  for (let i = 0; i < name.length; ++i) {
    if (name.charAt(i) === "-") result.push(" ");
    else {
      result.push(
        String.fromCharCode(97 + (name.charCodeAt(i) - 97 + shift) % 26),
      );
    }
  }
  return result.join("").trim();
};

const TEST = false;

if (TEST) {
  Deno.test("part1 sample", () => {
    const result = [
      "aaaaa-bbb-z-y-x-123[abxyz]",
      "a-b-c-d-e-f-g-h-987[abcde]",
      "not-a-real-room-404[oarel]",
      "totally-real-room-200[decoy]",
    ].map((line) => [name(line), digit(line), checksum(line)]).map((value) => {
      const [n, _d, c] = value;
      return validateChecksum(countAndSort(n as string), c as string);
    });
    assertEquals(result, [true, true, true, false]);
  });

  Deno.test("part2 sample", () => {
    const line = "qzmt-zixmtkozy-ivhz-343";
    const [n, d, c] = [name(line, false), digit(line), checksum(line)];
    assertEquals(decrypt(n, d), "very encrypted name");
  });
} else {
  const input = await Deno.readTextFile("../inputs/input04");
  const sumRoomIds = input.split("\n").map((
    line,
  ) => [name(line), digit(line), checksum(line)]).reduce((acc, value) => {
    const [n, d, c] = value;
    const validationResult = validateChecksum(
      countAndSort(n as string),
      c as string,
    );
    if (validationResult) {
      return acc + (d as number);
    }
    return acc;
  }, 0);
  console.log(`Part 1: ${sumRoomIds}`);

  const decryptedNamesSectorIds = input.split("\n").map((
    line,
  ) => [decrypt(name(line, false), digit(line)), digit(line)]);
  for (const value of decryptedNamesSectorIds) {
    console.log(value);
  }
}
