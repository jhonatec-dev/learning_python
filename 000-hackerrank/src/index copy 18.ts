function angryProfessor(k: number, a: number[]): string {
  // Write your code here
  const n = a.length;
  let result = "YES";

  const onTime = a.filter((arrive) => arrive < 1).length;
  // console.log('ontime', onTime)
  if (onTime >= k) {
    return "NO";
  }

  return result;
}

const k = 3;
const a = [-1, -3, 4, 2];
console.log(angryProfessor(k, a));
