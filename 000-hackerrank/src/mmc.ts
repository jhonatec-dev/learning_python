export default function mmc(arr: number[]): number {
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

//console.log(mmc([3976, 988]));
