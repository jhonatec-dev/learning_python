function gradingStudents(grades: number[]): number[] {
  // Write your code here

  return grades.map((grade) => {
    if (grade < 38) {
      return grade;
    }

    let nextMultipleOfFive = grade;
    while (nextMultipleOfFive % 5 !== 0) {
      nextMultipleOfFive += 1;
    }

    if (nextMultipleOfFive - grade < 3) {
      return nextMultipleOfFive;
    }

    return grade;
  });
}

console.log(gradingStudents([73, 67, 38, 33]));
