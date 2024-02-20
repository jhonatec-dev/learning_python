/*
 * Complete the 'bonAppetit' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY bill
 *  2. INTEGER k
 *  3. INTEGER b
 */

function bonAppetit(bill: number[], k: number, b: number): void {
  // Write your code here
  const annaBill =
    bill.reduce((acc, num, index) => (index === k ? acc : acc + num), 0) / 2;

  const message = annaBill === b ? "Bon Appetit" : (b - annaBill).toString();
  console.log(message);
}

const bill = [3, 10, 2, 9];
const k = 1;
const b = 7;

bonAppetit(bill, k, b);
