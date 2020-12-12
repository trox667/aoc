import * as fs from "fs";
import {
  BoxGeometry,
  Mesh,
  MeshBasicMaterial,
  PerspectiveCamera,
  Scene,
  WebGLRenderer,
} from "three";

class Visualization {
  public scene: Scene;
  public renderer: WebGLRenderer;
  public camera: PerspectiveCamera;
  private data: Array<Array<Mesh>>;
  private red: MeshBasicMaterial;
  private green: MeshBasicMaterial;
  private grey: MeshBasicMaterial;

  constructor() {
    this.scene = new Scene();
    this.camera = new PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000
    );
    this.renderer = new WebGLRenderer();
    this.renderer.setClearColor(0xffffff);
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.append(this.renderer.domElement);
    this.camera.position.z = 100;

    this.red = new MeshBasicMaterial({ color: 0xff0000 });
    this.green = new MeshBasicMaterial({ color: 0x00ff00 });
    this.grey = new MeshBasicMaterial({ color: 0xcccccc });
  }

  initGrid(width: number, height: number) {
    this.camera.position.x = width / 2 - 0.5;
    this.camera.position.y = -(height / 2 - 0.5);
    this.data = new Array<Array<Mesh>>();
    for (let y = 0; y < height; y++) {
      const row = new Array<Mesh>();
      for (let x = 0; x < width; x++) {
        const geometry = new BoxGeometry(0.5, 0.5);

        const cube = new Mesh(geometry, this.grey);
        cube.position.x = x;
        cube.position.y = -y;
        this.scene.add(cube);
        row.push(cube);
      }
      this.data.push(row);
    }
  }

  updateGrid(grid: Grid) {
    for (let y = 0; y < grid.height; y++) {
      for (let x = 0; x < grid.width; x++) {
        const s = grid.get(x, y);
        const mesh = this.data[y][x];
        switch (s) {
          case Seat.Taken:
            mesh.material = this.red;
            break;
          case Seat.Free:
            mesh.material = this.green;
            break;
          default:
            mesh.material = this.grey;
            break;
        }
      }
    }
  }

  render() {
    requestAnimationFrame(() => this.render());
    this.renderer.render(this.scene, this.camera);
  }
}

export function read_input(): Array<string> {
  return fs
    .readFileSync("../inputs/input11", "utf8")
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line.length > 0);
}

enum Seat {
  Taken,
  Free,
  Floor,
}

function seatFromString(s): Seat {
  if (s == "#") return Seat.Taken;
  else if (s == "L") return Seat.Free;
  else return Seat.Floor;
}

function seatToString(s): string {
  switch (s) {
    case Seat.Taken:
      return "#";
    case Seat.Free:
      return "L";
    default:
      return ".";
  }
}

class Grid {
  public data: Array<Array<Seat>>;
  public width: number;
  public height: number;
  constructor() {
    this.data = [];
    this.width = 0;
    this.height = 0;
  }

  init() {
    for (let y = 0; y < this.height; y++) {
      const row = new Array();
      for (let x = 0; x < this.width; x++) {
        row.push(Seat.Floor);
      }
      this.data.push(row);
    }
  }

  put(x: number, y: number, value: Seat) {
    if (x >= 0 && x < this.width && y >= 0 && y < this.height)
      this.data[y][x] = value;
  }

  cloneEmpty(): Grid {
    const g = new Grid();
    g.width = this.width;
    g.height = this.height;
    g.init();
    for (let y = 0; y < g.height; y++) {
      for (let x = 0; x < g.width; x++) {
        g.put(x, y, Seat.Floor);
      }
    }
    return g;
  }

  get(x: number, y: number): Seat {
    if (x >= 0 && x < this.width && y >= 0 && y < this.height)
      return this.data[y][x];
    return null;
  }

  countTaken(): number {
    let count = 0;
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        if (this.get(x, y) == Seat.Taken) count++;
      }
    }
    return count;
  }

  draw() {
    for (let y = 0; y < this.height; y++) {
      let row = "";
      for (let x = 0; x < this.width; x++) {
        row += seatToString(this.get(x, y));
      }
      console.log(row);
    }
  }
}

function createGrid(lines: Array<string>): Grid {
  lines = lines.filter((line) => line.length > 0).map((line) => line.trim());
  const g = new Grid();
  g.width = lines[0].length;
  g.height = lines.length;
  g.init();
  let y = 0;
  for (const line of lines) {
    for (let x = 0; x < line.length; x++) {
      const s = line.charAt(x);
      g.put(x, y, seatFromString(s));
    }
    y++;
  }
  return g;
}

function adjacentSeats(grid: Grid, x: number, y: number, infinite = true) {
  let count = 0;
  const dirs = [
    [-1, 1],
    [0, 1],
    [1, 1],
    [-1, 0],
    [1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
  ];

  for (const dir of dirs) {
    let [dx, dy] = dir;
    let scale = 1;
    let checkPos = [x + dx * scale, y + dy * scale];
    while (grid.get(checkPos[0], checkPos[1]) !== null) {
      const c = grid.get(checkPos[0], checkPos[1]);
      if (c == Seat.Taken) {
        count++;
        break;
      } else if (c == Seat.Free) {
        break;
      }

      if (infinite) {
        scale++;
        checkPos = [x + dx * scale, y + dy * scale];
      } else {
        break;
      }
    }
  }
  return count;
}

function neighbors(grid: Grid, x: number, y: number) {
  return adjacentSeats(grid, x, y, false);
}
function inSight(grid: Grid, x: number, y: number) {
  return adjacentSeats(grid, x, y, true);
}

function applyRules(
  grid: Grid,
  newGrid: Grid,
  x: number,
  y: number,
  neighborFunc,
  maxAjacentSeats: number
) {
  const nc = neighborFunc(grid, x, y);
  const seat = grid.get(x, y);
  if (seat == Seat.Free && nc == 0) {
    newGrid.put(x, y, Seat.Taken);
  } else if (seat == Seat.Taken && nc >= maxAjacentSeats) {
    newGrid.put(x, y, Seat.Free);
  } else {
    newGrid.put(x, y, seat);
  }
}

function turn(grid: Grid, neighborFunc, maxAjacentSeats: number): Grid {
  const newGrid = grid.cloneEmpty();
  for (let y = 0; y < newGrid.height; y++) {
    for (let x = 0; x < newGrid.width; x++) {
      applyRules(grid, newGrid, x, y, neighborFunc, maxAjacentSeats);
    }
  }
  return newGrid;
}

export function run(
  input: Array<string>,
  neighborFunc,
  maxAjacentSeats: number
) {
  let grid = createGrid(input);
  const visu = new Visualization();
  visu.initGrid(grid.width, grid.height);
  console.log(grid.width, grid.height);
  visu.render();
  visu.updateGrid(grid);

  const id = setInterval(() => {
    const newGrid = turn(grid, neighborFunc, maxAjacentSeats);
    visu.updateGrid(newGrid);
    if (JSON.stringify(grid.data) == JSON.stringify(newGrid.data)) {
      clearInterval(id);
      document.querySelector("#p1").innerHTML = "" + newGrid.countTaken();
      // return newGrid.countTaken();
    }
    grid = newGrid;
  }, 50);

  // while (true) {
  //   const newGrid = turn(grid, neighborFunc, maxAjacentSeats);
  //   if (JSON.stringify(grid.data) == JSON.stringify(newGrid.data)) {
  //     return newGrid.countTaken();
  //   }
  //   grid = newGrid;
  // }
}

function test() {
  const input = `L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL`;
  run(input.split("\n"), neighbors, 4);
}
// test();

function part1() {
  fetch("input11")
    .then((res) => res.text())
    .then((txt) => {
      run(txt.split("\n"), neighbors, 4);
    });
}

function part2() {}
part1();

console.log("Day 11");
