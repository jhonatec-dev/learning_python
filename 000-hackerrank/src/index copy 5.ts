function breakingRecords(scores: number[]): number[] {
  // Write your code here
  let lowScore = scores[0];
  let highScore = scores[0];
  let countLow = 0;
  let countHigh = 0;

  scores.forEach((score) => {
    if (score > highScore) {
      highScore = score;
      countHigh += 1;
    } else if (score < lowScore) {
      lowScore = score;
      countLow += 1;
    }
  });

  return [countHigh, countLow];
}

console.log("result", breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]));
console.log(
  "result",
  breakingRecords("10 5 20 20 4 5 2 25 1".split(" ").map((c) => +c))
);
