# Write a program to print the character along with its frequency ( Frequency- Number of time the character is occurred in the string )
"""
**Example:**

Input : aaabbaccd

Output : a3b2ac2d

To print each character along with its frequency from a given string, you can follow this approach:

1. **Traverse the String**: Go through each character in the string.
2. **Character Count**: Keep a count of each character's occurrence, similar to the previous solution. You can use a dictionary for this.
3. **Generate the Output**: Create a string that includes each character and its count from the dictionary.

However, a direct implementation of this might not work as expected for strings with consecutive repeating characters, like in your example "aaabbaccd". To handle this, we need to modify the approach slightly:

- **Track Consecutive Characters**: As we traverse the string, keep track of the current character and its count. If the next character is different, add the current character and its count to the output string and reset the count.
"""
def charFrequencyString(word):
    string = ""
    currentChar = word[0]
    charCount = 1
    for i in word[1:]:
        if i==currentChar:
            charCount+=1
        else:
            string+=currentChar+str(charCount)
            currentChar = i
            charCount=1
    string += currentChar + str(charCount)
    return string


# word = "aaabbaccdd"
word = input("Enter your word: ")
output = charFrequencyString(word)
print(output)