function sockMerchant(n: number, ar: number[]): number {
  // Write your code here

  // create a set with all occurrences
  let counts: { [key: string]: number } = {};
  ar.forEach((num) => {
    if (counts[num]) {
      counts[num] += 1;
    } else {
      counts[num] = 1;
    }
  });

  const pairs = Object.values(counts).reduce(
    (acc, num) => acc + Math.floor(num / 2),
    0
  );
  return pairs;
}

const ar = [10, 20, 20, 10, 10, 30, 50, 10, 20];
const n = ar.length;

console.log(sockMerchant(n, ar));
