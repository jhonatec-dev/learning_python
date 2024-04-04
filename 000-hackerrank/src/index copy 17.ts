function utopianTree(n: number): number {
  // Write your code here
  let result = 1;
  const isEven = (num: number) => num % 2 === 0;
  // 1 -> dbl (odd)
  // 2 -> +1 (even)
  for (let index = 1; index <= n; index++) {
    if (isEven(index)) {
      result += 1;
    } else {
      result *= 2;
    }
  }

  return result;
}

console.log(utopianTree(0)); // 1
console.log(utopianTree(1)); // 1
console.log(utopianTree(2)); // 1
console.log(utopianTree(3)); // 1
console.log(utopianTree(4)); // 1
console.log(utopianTree(5)); // 1
console.log(utopianTree(6)); // 1
