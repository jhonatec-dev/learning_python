/*
 * Complete the 'kangaroo' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER x1
 *  2. INTEGER v1
 *  3. INTEGER x2
 *  4. INTEGER v2
 */

function kangaroo(x1: number, v1: number, x2: number, v2: number): string {
  // Write your code here
  if (x2 > x1) {
    if (v2 > v1) return "NO";
  } else if (x1 > x2) {
    if (v1 > v2) return "NO";
  }

  const isEven = (num: number) => num !== 0 && num % 2 === 0;
  const firstKangaroo = isEven(x1) === isEven(v1);
  const secondKangaroo = isEven(x2) === isEven(v2);
  // console.log(firstKangaroo, secondKangaroo);
  if (firstKangaroo !== secondKangaroo) return "NO";

  let count = 0;
  while (true) {
    count += 1;
    const pos1 = x1 + v1 * count;
    const pos2 = x2 + v2 * count;
    // console.log(count, ": ", pos1, " - ", pos2);
    if (pos1 === pos2) {
      return "YES";
    }
    if (x2 > x1 && pos2 < pos1) {
      return "NO";
    }

    if (x1 > x2 && pos1 < pos2) {
      return "NO";
    }

    if (count > 10000) {
      return "NO";
    }
  }
}

console.log(kangaroo(0, 2, 5, 3)); //NO
console.log(kangaroo(43, 2, 70, 2)); // NO
console.log(kangaroo(0, 3, 4, 2)); // YES
console.log(kangaroo(4181, 3976, 6312, 988)); // NO
console.log(kangaroo(28, 8, 96, 2)); // NO
