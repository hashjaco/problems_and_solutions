def is_palindrome(word: str) -> bool:
    return word == word[::-1]


def make_palindrome(word: str) -> str:
    if is_palindrome(word):
        return word

    left, right = 0, len(word)-1
    while left < right:
        if word[right] != word[left]:
            # 1. somanyna => somanynas
            # 2. somanynas => somanynaos
            # 3. somanynaos => somanynamos
            # 4. somanynamos => is_palindrome
            word = f"{word[:right+1]}{word[left]}{word[right+1:]}"
        else:
            right -= 1
        left += 1
    return word


print(make_palindrome("somanyna"))
print(make_palindrome(""))
print(make_palindrome("somanyddynamos"))
print(make_palindrome("-+3jkf"))
