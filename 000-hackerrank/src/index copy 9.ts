/*
 * Complete the 'dayOfProgrammer' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER year as parameter.
 * return dd.mm.yyyy
 */

function dayOfProgrammer(year: number): string {
  // Write your code here
  let day,
    month = "09";

  // Isleap year
  function isLeapYear(year: number) {
    if (year < 1918) {
      return year % 4 === 0;
    }
    return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
  }

  if (year === 1918) {
    return "26.09.1918";
  }
  day = isLeapYear(year) ? "12" : "13";

  return `${day}.${month}.${year}`;
}

// const test = [1, 4, 4, 4, 5, 3];
const test = 1800;
console.log(dayOfProgrammer(test)); // 13.09.2017
