function pickingNumbers(a: number[]): number {
  // Write your code here
  // sorting
  a.sort((a, b) => a - b);
  // console.log(a);
  let pairs: number[][] = [];
  for (let out = 0; out < a.length; out += 1) {
    let found = false;
    let newPair: number[] = [];
    for (let inner = out + 1; inner < a.length; inner += 1) {
      const diff = Math.abs(a[out] - a[inner]);
      if (diff < 2) {
        newPair.push(a[inner]);
        found = true;
      }
    }
    if (found) {
      newPair.unshift(a[out]);
      pairs.push(newPair);
    }
  }
  const longestLenght = Math.max(...pairs.map((pair) => pair.length));
  return longestLenght;
}

const test = [4, 6, 5, 3, 3, 1];
console.log(pickingNumbers(test));
