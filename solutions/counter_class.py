from collections import defaultdict

def top_three_letters(string: str) -> [tuple]:
    """
       Given a string find the top three most frequent letters
       This method should return a list of tuples, where the tuple contains the character and count

       >>> top_three_letters("abbccc")
       [('c', 3), ('b', 2), ('a', 1)]

       >>> top_three_letters("aabbccdd")
       [('a', 2), ('b', 2), ('c', 2), ('d', 2)]
    """

    #  loop through the string and store the count for each letter
    #  sort the dictionary by the count and find the top three most frequent letters
    #  return a formatted list to match the output

    counter = defaultdict(int)
    for c in string:
        counter[c] += 1
    print(sorted(counter, key=lambda k: counter[k], reverse=True))


