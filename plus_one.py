"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
>>> plus_one([1, 2, 3])
[1, 2, 4]

Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
>>> plus_one([4, 3, 2, 1])
[4, 3, 2, 2]

Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [0]
>>> plus_one([0])
[1]

Explanation: The array represents the integer 0.
Incrementing by one gives 0 + 1 = 1.
Thus, the result should be [1].

Example 4:
Input: digits = [9]
>>> plus_one([9])
[1, 0]

Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

def plus_one(digits: [int]) -> [int]:
    if not digits:
        return []
    digitsToString = ''.join(str(i) for i in digits)
    integerPlusOne = str(int(digitsToString)+1)
    return [int(i) for i in integerPlusOne]


# def plus_one(digits: [int]) -> [int]:
#     return [int(i) for i in str(int(''.join(str(i) for i in digits))+1)]
