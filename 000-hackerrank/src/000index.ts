function timeConversion(s: string): string {
  // Write your code here
  const time = s.match(/(\d\d):(\d\d):(\d\d)/);
  const ending = s.match(/[A|P]M$/i);
  // console.log(time?.length)
  // console.log(ending);

  if (time && time?.length > 3) {
    if (ending) {
      if (ending[0].toUpperCase() === "PM") {
        if (+time[1] < 12) {
          const newHour = +time[1] + 12;
          const newHourString =
            newHour < 10 ? `0${newHour}` : newHour.toString();
          time[0] = `${newHourString}` + time[0].slice(2);
        }
      } else if (+time[1] === 12) {
        time[0] = '00' + time[0].slice(2);
      }
    }
    return time[0];
  }
  return "Falhei feio";
}

console.log("resultado", timeConversion("12:01:00AM"));
