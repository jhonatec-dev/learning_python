function countingValleys(steps: number, path: string): number {
  // Write your code here
  let valleys = 0;
  let level = 0;
  let seaLevel = true;
  path.split("").forEach((mov) => {
    level += mov === "U" ? 1 : -1;
    console.log("level", level, "mov", mov);
    if (seaLevel && level < 0) {
      seaLevel = false;
      valleys += 1;
    }
    seaLevel = level === 0;
  });

  return valleys;
}

//const steps = 8
const path = "UDDDUDUUDU";
const steps = path.length;

console.log(countingValleys(steps, path));
