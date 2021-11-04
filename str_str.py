"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
>>> str_str("hello", "ll")
2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
>>> str_str("aaaaa", "bba")
-1

Example 3:

Input: haystack = "", needle = ""
Output: 0
>>> str_str("", "")
0

Example 3:

Input: haystack = "", needle = ""
Output: 0
>>> str_str("mississippi", "issip")
4

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""


def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    n_chars_found, index_of_needle = 0, 0

    for hay_pos, hay_char in enumerate(haystack):
        if needle[n_chars_found] == hay_char:
            index_of_needle = hay_pos if n_chars_found == 0 else index_of_needle
            n_chars_found += 1
            if n_chars_found == len(needle):
                return index_of_needle
        else:
            n_chars_found = 0
    return -1

