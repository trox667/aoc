const input = "1321131112";

function run(runs: number): number {
  let tokens = input.split("");
  let newTokens = [];

  for (let k = 0; k < runs; ++k) {
    if (tokens.length == 1) {
      newTokens.push("1");
      newTokens.push(tokens[0]);
    } else {
      for (let i = 0; i < tokens.length; ++i) {
        let count = 1;
        const token = tokens[i];
        for (let j = i + 1; j < tokens.length; ++j) {
          if (token === tokens[j]) {
            count++;
            i++;
          } else {
            break;
          }
        }
        newTokens.push("" + count);
        newTokens.push(token);
      }
    }
    tokens = [...newTokens];
    newTokens = [];
  }
  return tokens.length;
}

console.log(`Part 1: ${run(40)}`);
console.log(`Part 2: ${run(50)}`);
