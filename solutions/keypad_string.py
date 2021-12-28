
"""
Given a string consisting of 0-9, find the string that is created using a standard phone keypad
| 1        | 2 (abc)   | 3 (def)  |
| 4 (ghi)  | 5 (jkl)   | 6 (mno)  |
| 7 (pqrs) | 8 (tuv)   | 9 (wxyz) |
|    *     | 0 ( )     |    #     |

You can ignore 1, and 0 corresponds to whitespace

>>> keypad_string("22598")
'bjwt'
>>> keypad_string("4433555555666")
'hello'
>>> keypad_string("")
''
>>> keypad_string("111")
''
"""

def add_char_from_keypad(key_chars: str, string_arr: list, index_of_char: int):
    string_arr.append(key_chars[index_of_char])


def get_keypad():
    import string
    letters = string.ascii_lowercase
    keys = string.digits
    keypad = {}
    start_index = 0
    for key in keys:
        if key == "0":
            keypad[key] = " "
        elif key == "1":
            keypad[key] = ""
        else:
            num_of_letters = 3
            if key in {"7", "9"}:
                num_of_letters = 4
            keypad[key] = letters[start_index:start_index+num_of_letters]
            start_index += num_of_letters
    return keypad


def keypad_string(keys: str) -> str:
    if not keys:
        return ""
    keypad = get_keypad()



test_string1 = "2233555555666"
test_string2 = ""
test_string3 = "22121229941444777555"
print(keypad_string(test_string1))
print(keypad_string(test_string2))
print(keypad_string(test_string3))
