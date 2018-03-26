# 1. Two Sum
# Python 3
# https://leetcode.com/problems/two-sum

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        delta = i + 1
        value = target - nums[i]
        if value in nums[delta:]:
            return [i, nums[delta:].index(value) + delta]

numbers, target = [2, 3, 4], 6
print(twoSum(numbers, target))