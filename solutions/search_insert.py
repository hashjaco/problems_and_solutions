def search(nums: [int], start: int, end: int, target: int) -> int:
    if start == end:
        return start if target < nums[start] else start + 1
    median = (start + end) // 2

    return median if nums[median] == target else search(nums, start, median, target) if target < nums[
        median] else search(nums, median + 1, end, target)


def search_insert(nums: [int], target: int) -> int:
    if not nums:
        return 0
    return search(nums, 0, len(nums)-1, target)
