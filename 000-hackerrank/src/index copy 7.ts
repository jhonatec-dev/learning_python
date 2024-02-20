function divisibleSumPairs(n: number, k: number, ar: number[]): number {
  // Write your code here
  let count = 0;
  ar.sort((a, b) => a - b);

  ar.forEach((num, index) => {
    for (let innerIndex = index + 1; innerIndex < ar.length; innerIndex += 1) {
      const sum = num + ar[innerIndex];
      if (sum % k === 0) {
        count += 1;
      }
    }
  });

  return count;
}

const test = [1, 3, 2, 6, 1, 2];
console.log(divisibleSumPairs(6, 3, test)); // 3
