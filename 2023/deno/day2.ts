// Read and parse input

// const input = await Deno.readTextFile("../input/sample02");
const input = await Deno.readTextFile("../input/input02");
const games = input
  .split("\n")
  .filter((line) => line.length > 0)
  .map((line) => {
    const [game, sets] = line.split(": ");
    const gameId = parseInt(game.replaceAll("Game ", ""));
    const gameSets = sets.split("; ").map((set) => {
      const result: Map<string, number> = new Map();
      set.split(", ").map((cube) => {
        const [count, color] = cube.split(" ");
        result.set(color, parseInt(count));
      });
      return result;
    });
    return { id: gameId, sets: gameSets };
  });

// Part 1: What is the sum of the IDs of those games that are not impossible?

const part1 = games
  .filter(
    (game) =>
      !game.sets.some(
        (set) =>
          (set.get("red") ?? 0) > 12 ||
          (set.get("green") ?? 0) > 13 ||
          (set.get("blue") ?? 0) > 14
      )
  )
  .reduce((acc, game) => acc + game.id, 0);

console.log("Part 1:", part1);

// Part 2: What is the sum of the power of the sets that have the fewest number of cubes of each color

const part2 = games.reduce((acc, game) => {
  let red = 0;
  let green = 0;
  let blue = 0;
  game.sets.forEach((set) => {
    red = Math.max(red, set.get("red") ?? 0);
    green = Math.max(green, set.get("green") ?? 0);
    blue = Math.max(blue, set.get("blue") ?? 0);
  });
  acc += red * green * blue;
  return acc;
}, 0);

console.log("Part 2:", part2);
