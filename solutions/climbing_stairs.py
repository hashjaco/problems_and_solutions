""" 70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
>>> climb_stairs(2)
2

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
>>> climb_stairs(3)
3

Constraints:

1 <= n <= 45
"""

def climb_stairs(n: int) -> int:
    memo = [0] * (n + 1)
    memo[0] = memo[1] = 1
    for idx, val in enumerate(memo):
        if val == 0:
            memo[idx] = memo[idx-1] + memo[idx-2]
    return memo[n]


print(climb_stairs(8))

