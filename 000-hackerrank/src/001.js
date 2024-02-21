function getMoneySpent(keyboards, drives, b) {
  /*
   * Write your code here.
   */
  let maxBudget = -1;

  keyboards = keyboards.filter((k) => k < b);
  drives = drives.filter((d) => d < b);

  keyboards.forEach((k) => {
    drives.forEach((d) => {
      const total = k + d;
      // console.log("total", total);
      if (total <= b && total > maxBudget) {
        maxBudget = total;
      }
    });
  });

  return maxBudget;
}

const keyboards = [3, 1];
const drives = [5, 2, 8];
const b = 10;

console.log(getMoneySpent(keyboards, drives, b));
