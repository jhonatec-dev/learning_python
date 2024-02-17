export default function mmc(arr: number[]): number {
  let exclusiveArr = Array.from(new Set(arr));
  const multiples: number[] = [];
  let mult = 2;
  while (exclusiveArr.every((num) => num !== 1)) {
    console.log("mult", mult, "arr", exclusiveArr, " multiples", multiples);
    const foundSomeMultiple = false;
    exclusiveArr = exclusiveArr.map((n) => {
      if (n % mult === 0) {
        if (!foundSomeMultiple) {
          multiples.push(mult);
          foundSomeMultiple = true;
        }
        return n / mult;
      }
      return n;
    });
    mult += 1;
  }
  console.log("mult", mult, "arr", exclusiveArr, " multiples", multiples);
  return multiples.reduce((acc, num) => acc * num, 1);
}

console.log(mmc([3, 6, 9]));
