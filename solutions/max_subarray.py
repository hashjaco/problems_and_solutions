"""
MAX SUBARRAY:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

EXAMPLE 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
>>> max_subarray([-2,1,-3,4,-1,2,1,-5,4])
6

EXAMPLE 2:
Input: nums = [1]
Output: 1
>>> max_subarray([1])
1

EXAMPLE 3:
Input: nums = [5,4,-1,7,8]
Output: 23
>>> max_subarray([5,4,-1,7,8])
23

CONSTRAINTS:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

FOLLOW-UP: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

def max_subarray(nums: [int]) -> int:
    curr_max = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)

    return max_sum
