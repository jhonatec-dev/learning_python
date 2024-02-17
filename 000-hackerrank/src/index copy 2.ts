/*
 * Complete the 'countApplesAndOranges' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER s
 *  2. INTEGER t
 *  3. INTEGER a
 *  4. INTEGER b
 *  5. INTEGER_ARRAY apples
 *  6. INTEGER_ARRAY oranges
 */

function countApplesAndOranges(
  s: number,
  t: number,
  a: number,
  b: number,
  apples: number[],
  oranges: number[]
): void {
  // Write your code here
  const fallenApples = apples.map((apple) => a + apple);
  const fallenOranges = oranges.map((orange) => b + orange);
  const targetApples = fallenApples.filter(
    (position) => position >= s && position <= t
  );
  const targetOranges = fallenOranges.filter(
    (position) => position >= s && position <= t
  );
  console.log(targetApples.length);
  console.log(targetOranges.length);
}

countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4]);
