function migratoryBirds(arr: number[]): number {
  // Write your code here
  const counts: { [key: string]: number } = {};

  // Counting the ocurrencies
  arr.forEach((num) => {
    if (counts[num]) {
      counts[num] += 1;
    } else {
      counts[num] = 1;
    }
  });

  // Find the highest value
  const highValue = Math.max(...Object.values(counts));

  // Find the [key, value] who matches
  const keys = Object.entries(counts).filter(
    ([_key, value]) => value === highValue
  );

  // Find the lowest key
  const result = Math.min(...keys.map(([key, _value]) => +key));

  return result;
}

// const test = [1, 4, 4, 4, 5, 3];
const test = [1, 1, 2, 2, 3];
console.log(migratoryBirds(test)); // 3
