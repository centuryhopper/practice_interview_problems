interface Point {
  x: number;
  y: number;
}

function distance(p1: Point, p2: Point): number {
  return Math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2);
}

function travelingSalesman(points: Point[]): number {
  const n = points.length;
  let min = Number.MAX_VALUE;

  function visit(path: number[], remaining: number[]) {
    if (remaining.length === 0) {
      let d = 0;
      for (let i = 0; i < n - 1; i++) {
        d += distance(points[path[i]], points[path[i + 1]]);
      }
      d += distance(points[path[n - 1]], points[path[0]]);
      min = Math.min(min, d);
    } else {
      for (const i of remaining) {
        const nextRemaining = remaining.filter((j) => j !== i);
        visit([...path, i], nextRemaining);
      }
    }
  }

  visit([0], [...Array(n).keys()].slice(1));

  return min;
}

const cities = [
  { name: 'A', x: 0, y: 0 },
  { name: 'B', x: 1, y: 1 },
  { name: 'C', x: 2, y: 2 },
  { name: 'D', x: 3, y: 3 },
];

let result = travelingSalesman(cities);
console.log(result)
result = travelingSalesman([]);
console.log(result)
result = travelingSalesman([cities[0]]);
console.log(result)





