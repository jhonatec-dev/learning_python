function hurdleRace(k: number, height: number[]): number {
  // Write your code here
  let result = 0;
  const maxHeight = Math.max(...height);
  if (maxHeight > k) {
    result = maxHeight - k;
  }

  return result;
}
