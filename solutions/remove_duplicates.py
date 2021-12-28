def remove_duplicates(nums: [int]):
    k = 0
    for num in nums:
        if num != nums[k]:
            nums[k+1] = num
            k += 1
    return k+1


nums_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums_list2 = [-1, 0, 0, 0, 0, 3, 3]
k1 = remove_duplicates(nums_list)
k2 = remove_duplicates(nums_list2)
print(f"{k1}, {nums_list}\n")
print(f"{k2}, {nums_list2}\n")
