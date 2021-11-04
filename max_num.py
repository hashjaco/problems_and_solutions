def max_num(arr: [int]) -> int:
    max_number = float('-inf')
    for num in arr:
        breakpoint()
        max_number = num if num > max_number else max_number
    return max_number

