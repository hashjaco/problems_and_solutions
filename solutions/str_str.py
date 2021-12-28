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
# def str_str(haystack: str, needle: str) -> int:
#     if len(needle) == 0:
#         return 0
#     for i, char in enumerate(haystack):
#         if i + len(needle) > len(haystack):
#             return -1
#         if haystack[i:i+len(needle)] == needle:
#             return i
#     return -1


def str_str(haystack: str, needle: str) -> int:
    return haystack.index(needle) if needle in haystack else -1

