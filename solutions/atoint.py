def myAtoi(s: str) -> int:
    if not s:
        return 0

    MIN_INT = pow(-2, 31)
    MAX_INT = pow(2, 31) - 1

    sign = 1
    integer = []
    index = 0

    # pass over leading whitespace
    while index < len(s) and s[index] == ' ':
        index += 1

    if index >= len(s):
        return 0

    while s[index] == '-' or s[index] == '+':
        sign = -1 if s[index] == '-' else 1
        index += 1
        break

    while index < len(s) and s[index].isdigit():
        integer.append(s[index])
        index += 1

    s = ''.join(integer)

    if s:
        s = sign * int(s)
        if s < MIN_INT:
            return MIN_INT
        if s > MAX_INT:
            return MAX_INT
        return s
    return 0


test1 = "42"
test2 = "   -42"
test3 = "4193 with words"
test4 = "words and 987"
test5 = "-91283472332"
test6 = "00000-42a1234"
test7 = " "

print(myAtoi(test7))
