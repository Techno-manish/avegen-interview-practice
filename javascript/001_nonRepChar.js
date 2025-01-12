//  Write a program to print first non repeating character of a string
/*
**Example:**

Input :  amazon

Output : m

To solve the problem of finding the first non-repeating character in a string, we can follow these steps:

1. **Traverse the String**: Go through each character in the string.
2. **Character Count**: Keep a count of each character's occurrence. This can be efficiently done using a dictionary in Python.
3. **Find the Non-Repeating Character**: Traverse the string again and use the dictionary to check the count of each character. The first character with a count of 1 is the non-repeating character.

Here's the implementation in JavaScript:
*/

const firstNonRepChar = (word) => {
  const charCount = {};
  for (let char of word) {
    if (char in charCount) {
      charCount[char] += 1;
    } else {
      charCount[char] = 1;
    }
  }

  for (char of word) {
    if (charCount[char] === 1) {
      return char;
    }
  }
  return "No such char";
};

const word = "amazon";
// const word = "aabbcc";

output = firstNonRepChar(word);
console.log(output);
