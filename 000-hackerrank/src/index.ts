function designerPdfViewer(h: number[], word: string): number {
  // Write your code here
  const noSpacesWord = word.split(" ").join("");
  let tallestHeigh = 0;
  let result = 0;
  noSpacesWord.split("").forEach((char) => {
    const charIndex = char.charCodeAt(0) - 97;
    const charHeight = h[charIndex];
    if (charHeight > tallestHeigh) {
      tallestHeigh = charHeight;
    }
  });
  result = tallestHeigh * noSpacesWord.length;
  return result;
}

/*
All letters = 1mm wide
Example
h=[1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5]
word=' abc'

The heights are a=1 b=3 c=1
The talleste letter is 3 heigh and there are 3 letters

Result = 3 * 3
Resulta = 9mm2 (square)
*/

const h = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5"
  .split(" ")
  .map((char) => +char);
const word = " abc";

console.log(designerPdfViewer(h, word));
