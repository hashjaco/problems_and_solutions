""" Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
>>> add_binary("1010", "1011")
'10101'


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

Algorithm:
compare each digit from back to front.
if a[i] and b[i] = 0 a[i] + b[i] = 0
else if a[i] is 1 and b[i] is 0, and vice versa, then a[i] + b[i] =
"""


def add_binary(a: str, b: str) -> str:
    pass
