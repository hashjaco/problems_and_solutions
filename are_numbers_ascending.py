def are_numbers_ascending(s: str) -> bool:
    s = list(map(lambda dig: int(dig), filter(lambda char: char.isnumeric(), s.split(' '))))
    print(s)
    if len(s) < 2:
        return True
    prev = float("-Inf")
    for digit in s:
        if digit <= prev:
            return False
        prev = digit
    return True


test1 = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
test2 = "hello world 5 x 5"
test3 = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
test4 = "4 5 11 26"


print(are_numbers_ascending(test1))
print(are_numbers_ascending(test2))
print(are_numbers_ascending(test3))
print(are_numbers_ascending(test4))
print(are_numbers_ascending(" "))
print(are_numbers_ascending(""))
