import string

ascii_for_A = ord('A')
ascii_for_a = ord('a')
upper_word = "FALLOWS"
not_an_upper_word = "FAllows"

upper_alpha = string.ascii_uppercase

print("Hello world".isupper())

print(ascii_for_a)
print(ascii_for_A)
print(upper_alpha)

uppercase_set = set(upper_alpha)
print(uppercase_set)

def is_upper(word: str):
    for c in word:
        if c not in uppercase_set:
            return False
    return True


print(is_upper(upper_word))
print(is_upper(not_an_upper_word))
