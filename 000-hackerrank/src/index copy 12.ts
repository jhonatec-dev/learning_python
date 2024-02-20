function pageCount(n: number, p: number): number {
  // Write your code here
  let flips = [0, 0];
  // generate a book structure [[0,1], [2, 3], [4,5], [6]] ...
  let book: number[][] = [];
  for (let i = 0; i <= n; i += 2) {
    book.push([i, i + 1]);
  }
  // console.log(book);
  // flip from the start
  for (let i = 0; i < book.length; i += 1) {
    // console.log(book[i]);
    if (book[i].includes(p)) {
      flips[0] = i;
      break;
    }
  }
  // flip from the end
  for (let i = 0; i < book.length; i += 1) {
    if (book[book.length - (i + 1)].includes(p)) {
      flips[1] = i;
      break;
    }
  }

  // console.log("flips", flips);

  return Math.min(...flips);
}

const n = 5; // pages
const p = 3; // target page

console.log(pageCount(n, p));
