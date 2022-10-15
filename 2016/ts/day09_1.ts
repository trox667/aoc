enum TokenState {
  Value,
  Marker,
}

enum MarkerTokens {
  Open = "(",
  Close = ")",
  Separator = "x",
}

function convertInput(input: string, skipInternalMarker = true) {
  let pos = 0;
  let tokenState = TokenState.Value;
  let count = 0;
  let repeat = 0;
  let tmp = "";

  let decompressedLength = 0;

  while (pos < input.length) {
    const curr = input.charAt(pos);
    if (tokenState === TokenState.Value) {
      if (curr === MarkerTokens.Open) {
        tokenState = TokenState.Marker;
      } else {
        decompressedLength++;
      }
    } else {
      if (curr === MarkerTokens.Close) {
        repeat = parseInt(tmp);
        tmp = "";
        tokenState = TokenState.Value;
        if (skipInternalMarker) {
          const currDecompressedLength =
            input.substring(pos, pos + count).length * repeat;
          decompressedLength += currDecompressedLength;
          pos += count;
        } else {
          const currDecompressedLength = convertInput(
            input.substring(pos + 1, pos + 1 + count),
            skipInternalMarker,
          ) * repeat;
          decompressedLength += currDecompressedLength;
          pos += count;
        }
      } else if (curr === MarkerTokens.Separator) {
        count = parseInt(tmp);
        tmp = "";
      } else {
        tmp += curr;
      }
    }
    pos++;
  }
  return decompressedLength;
}

const input = await Deno.readTextFile("../inputs/input09");
console.log(
  `Part 1: ${
    convertInput(input.split("\n").filter((line) => line.length > 0).join(""))
  }`,
);
console.log(
  `Part 2: ${
    convertInput(
      input.split("\n").filter((line) => line.length > 0).join(""),
      false,
    )
  }`,
);
