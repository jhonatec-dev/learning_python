/*
A password string, pwd, consists of binary characters (0s and 1s).
A cyber securtity expert is trying to determine
the minimum number of changes required to make the password secure.
To do so it must be divided into subtrinsgs of non-overlaping,
even length substrings.
Each substring can only contain 1s or 0s, not a mix.
This helps to ensure that the password is strong
and less vulnerable to hacking attacks.

Find the minimum number of characters that must be lipped
in the password string,
changed from 0 to 1 or 1 to 0 to allow
the string to be divided as described.

Example:
Given pwd = "1110011000""
After the flips, remains two substrings: "11111111" and "00"
The two substrings have lengths 8 and 2 respectively.
Since both lengths are even, the division is valid.
So the answer should be 3

*/

const isReady = (chars: string[]) => {
  const firstChar = chars[0];
  for (let i = 1; i < chars.length; i++) {
    const char = chars[i];
    if (char !== firstChar) {
      if (i % 2 == 0) {
        const finalSubString = chars.slice(i, chars.length);
        return !finalSubString.includes(firstChar);
      } else return false;
    }
  }
  return false;
};

const min_flips_to_secure = (pwd: string) => {
  const flips = [0, 0];

  for (let loop = 0; loop < 2; loop += 1) {
    const chars = pwd.split("");
    const target_char = loop === 0 ? "0" : "1";
    const change_to = loop === 0 ? "1" : "0";
    for (let index = 0; index < chars.length; index += 1) {
      const char = chars[index];
      if (char == target_char) {
        flips[loop] += 1;
        chars[index] = change_to;
      }
      if (isReady(chars)) break;
    }
  }
  return Math.min(...flips);
};

const pwd = "1110011000";
const result = min_flips_to_secure(pwd);
console.log(`The result is ${result}`);
