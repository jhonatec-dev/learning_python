function birthday(s: number[], d: number, m: number): number {
  // Write your code here
  let found = 0;
  // m = length of items
  // d = target sum
  while (s.length >= m) {
    const target = s.slice(0, m);
    s.shift()
    console.log("target", target);
    const sum = target.reduce((sum, num) => sum + num, 0);
    if (sum === d) {
      found += 1;
    }
  }

  return found;
}

const example = [1, 2, 1, 3, 2];
console.log(birthday(example, 3, 2));
