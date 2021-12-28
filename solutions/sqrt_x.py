""" 69. SQRT(X)
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:
Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""

test = [4, 2, 9, 27, 49]


def my_sqrt(x: int) -> int:
    low, mid, high = 0, 0, x
    while low < high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            low = mid + 1
        else:
            high = mid - 1
    return high - 1 if high * high > x else high


for i in test:
    print(my_sqrt(i))

