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


# loop through array incrementing the size of subarray being checked each loop
# example:
# nums = [5,4,-1,7,8]
# loop 1: size of sub-arrays = 1
# 1: [5] => curr_max = [0:1]
# 2: [4] => curr_max = [0:1]
# 3: [-1] => curr_max = [0:1]
# 4: [7] => curr_max = [3:4]
# 5: [8] => curr_max = [4:]
# loop 2: size of sub-arrays = 2
# 1: [5,4] => curr_max = [0:2]
# 2: [4,-1] => curr_max = [0:2]
# ...... you get the point
# TODO: Refactor
def max_subarray(nums: [int]) -> int:
    max_arr_sum = float("-inf")
    start, end = 0, 1

    while end < len(nums) + 1:
        curr_sub = nums[start:end]
        if sum(curr_sub) > max_arr_sum:
            max_arr_sum = sum(curr_sub)
        else:
            start += 1
        print(max_arr_sum)
        end += 1
    return max_arr_sum
