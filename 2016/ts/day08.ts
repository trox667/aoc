enum Action {
  Rectangle,
  Column,
  Row,
}

type Data = [number, number];

const parseLine = (input: string): [Action, Data] | undefined => {
  if (input.indexOf("rect") !== -1) {
    const values = input.split(" ")[1].split("x").map((token) =>
      parseInt(token)
    );
    return [Action.Rectangle, values as [number, number]];
  } else if (input.indexOf("column") !== -1) {
    const tokens = input.split(" ");
    const x = parseInt(tokens[2].split("=")[1]);
    const by = parseInt(tokens[4]);
    return [Action.Column, [x, by]];
  } else if (input.indexOf("row") !== -1) {
    const tokens = input.split(" ");
    const y = parseInt(tokens[2].split("=")[1]);
    const by = parseInt(tokens[4]);
    return [Action.Row, [y, by]];
  }
  return undefined;
};

const display: string[][] = [];
// const HEIGHT = 3;
// const WIDTH = 7;
const HEIGHT = 6;
const WIDTH = 50;

for (let y = 0; y < HEIGHT; ++y) {
  const row = [];
  for (let x = 0; x < WIDTH; ++x) {
    row.push(" ");
  }
  display.push(row);
}

const drawDisplay = (display: string[][]) => {
  console.log(
    "------------------------------------------------------------",
  );
  for (let y = 0; y < HEIGHT; ++y) {
    console.log(display[y].join(""));
  }
};

drawDisplay(display);

const applyAction = (display: string[][], [action, data]: [Action, Data]) => {
  if (action === Action.Rectangle) {
    const [width, height] = data;
    for (let h = 0; h < height; ++h) {
      for (let w = 0; w < width; ++w) {
        display[h][w] = "#";
      }
    }
  } else if (action === Action.Column) {
    const [x, by] = data;
    const newColumn = [];
    for (let h = 0; h < HEIGHT; ++h) newColumn.push(" ");
    for (let h = 0; h < HEIGHT; ++h) {
      const idx = h + by >= HEIGHT ? h + by - HEIGHT : h + by;
      newColumn[idx] = display[h][x];
    }
    for (let h = 0; h < HEIGHT; ++h) display[h][x] = newColumn[h];
  } else if (action === Action.Row) {
    const [y, by] = data;
    const newColumn = [];
    for (let w = 0; w < WIDTH; ++w) newColumn.push(" ");
    for (let w = 0; w < WIDTH; ++w) {
      const idx = w + by >= WIDTH ? w + by - WIDTH : w + by;
      newColumn[idx] = display[y][w];
    }
    for (let w = 0; w < WIDTH; ++w) display[y][w] = newColumn[w];
  }
};

const countLitPixels = (display: string[][]): number => {
  return display.map((row) => row.filter((pixel) => pixel === "#")).flat(1)
    .length;
};

// const rect = parseLine("rect 3x2");
// if (rect) applyAction(display, rect);

// drawDisplay(display);

// const rotateX = parseLine("rotate column x=1 by 1");
// if (rotateX) applyAction(display, rotateX);

// drawDisplay(display);

// const rotateY = parseLine("rotate row y=0 by 4");
// if (rotateY) applyAction(display, rotateY);

// drawDisplay(display);

// const rotateX2 = parseLine("rotate column x=1 by 1");
// if (rotateX2) applyAction(display, rotateX2);

// drawDisplay(display);

// console.log(countLitPixels(display));

const input = await Deno.readTextFile("../inputs/input08");
input.split("\n").filter((line) => line.length > 0).map((line) =>
  parseLine(line)
).forEach((action) => {
  if (action) {
    applyAction(display, action);
    drawDisplay(display);
  }
});

drawDisplay(display);
console.log(countLitPixels(display));
