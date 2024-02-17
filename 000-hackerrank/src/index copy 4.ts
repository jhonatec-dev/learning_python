/*
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

function getTotalX(a: number[], b: number[]): number {
  function mmc(arr: number[]): number {
    let exclusiveArr = Array.from(new Set(arr));
    const multiples: number[] = [];
    let mult = 2;
    while (true) {
      if (exclusiveArr.every((num) => num === 1)) {
        break;
      }
      let foundSomeMultiple = false;
      exclusiveArr = exclusiveArr.map((n) => {
        if (n > 1 && n % mult === 0) {
          if (!foundSomeMultiple) {
            multiples.push(mult);
            foundSomeMultiple = true;
          }
          return n / mult;
        }
        return n;
      });
      if (foundSomeMultiple) {
        mult = 2;
      } else {
        mult += 1;
      }
    }
    return multiples.reduce((acc, num) => acc * num, 1);
  }
  // Write your code here
  const aExclusive = Array.from(new Set(a));
  aExclusive.sort((a, b) => a - b);
  // const commomMultiple = aExclusive.reduce((acc, num) => acc * num, 1);
  const commomMultiple = mmc(a);
  // console.log(aExclusive, commomMultiple);
  let multiples: number[] = [];

  let i = 1;
  let target = aExclusive[aExclusive.length - 1];
  // console.log(`i: ${i} | target: ${target}`);

  if (b.every((num) => num % target === 0)) {
    if (aExclusive.every((num) => target % num === 0)) multiples.push(target);
  }
  target = commomMultiple;
  while (true) {
    // console.log(`i: ${i} | target: ${target}`);
    target *= i;

    if (target > Math.max(...b)) {
      break;
    }
    // console.log(`b: ${b} | target: ${target}`);
    if (b.every((num) => num % target === 0)) {
      multiples.push(target);
    }
    target = commomMultiple;
    i += 1;
  }
  // console.log("multiples", multiples);
  const exclusiveMultipes = Array.from(new Set(multiples));
  return exclusiveMultipes.length;
}

const a = [3, 9, 6];
const b = [36, 72];
console.log(getTotalX(a, b)); // 8
