"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
0 <= n <= 30
"""
from functools import lru_cache


def fib_naive_recursive(n: int) -> int:
    return 0 if n < 1 else 1 if n < 3 else fib_naive_recursive(n-1) + fib_naive_recursive(n-2)


def fib_memoized_recursive(n: int) -> int:
    cache = {}

    def fib(memo, curr):
        if curr < 1:
            return 0
        if curr in memo:
            return memo[curr]
        value = 1 if curr < 3 else fib(memo, curr - 1) + fib(memo, curr - 2)
        memo[curr] = value
        return value

    return fib(cache, n)


@lru_cache(maxsize=1000)
def fib_lru_cached_recursive(n: int) -> int:
    return 0 if n < 1 else 1 if n < 3 else fib_lru_cached_recursive(n-1) + fib_lru_cached_recursive(n-2)


def fib_iterative(n: int):
    pass
