"""
Length of Last Word
Step 1: Understand the problem
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

Step 2: Ask Questions
1) Do the white spaces count in the length of the string s?
2) Does a single letter count as a word?
3) should punctuation be excluded from words, such as a period at the end of a sentence?
4) Does a hyphenated word count as one word?

Step 3: Write some test cases
>>> len_of_last_word("Hello World")
5

>>> len_of_last_word("   fly me   to   the moon  ")
4

>>> len_of_last_word("luffy is still joyboy")
6

>>> len_of_last_word("luffy is still joy-boy.")
7

>>> len_of_last_word("     ")
0


Step 4: Come up with a brute force solution
1) create two empty string variables, one to store current word, and one to create words with called next word.
2) loop through string s, appending characters to the end of the string variable that was create
3) if the current character is whitespace, set current word to next word if the length is greater than 0.
    otherwise, append the current character to new word.
4) When the end of the string s is reached, if next word is a valid word, return it, otherwise, return current word.
"""

# def len_of_last_word(s: str) -> int:
#     s = s.strip(' .')
#     curr_word = ""
#     next_word = ""
#     for letter in s:
#         if letter not in ['.', ' ']:
#             next_word += letter
#         else:
#             curr_word = next_word
#             next_word = ""
#     return len(next_word) if next_word else len(curr_word)


def len_of_last_word(s: str) -> int:
    s = s.strip(' .').split()
    return 0 if not s else len(s[len(s)-1])
