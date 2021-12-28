"""
Sorting the Sentence

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Example 1:

>>> sortSentence("is2 sentence4 This1 a3")
'This is a sentence'

Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

Example 2:

>>> sortSentence("Myself2 Me1 I4 and3")
'Me Myself and I'

Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
"""

##############

"""
Algorithm:
My first thought is to split the string by whitespace, storing every word in a list. 
Then loop through and insert each word into a dictionary with the last character ( the number ) as its key.
Then loop through the dictionary in order of position and append to a string.
Return the string in the end.
"""

def sort_sentence(s: str) -> str:
    s = s.split(" ")
    pos_dict = {word[-1:]: word[:-1] for word in s}
    for pos in range(len(s)):
        s[pos] = pos_dict[str(pos+1)]
    return " ".join(s)


print(sort_sentence("Myself2 Me1 I4 and3"))
