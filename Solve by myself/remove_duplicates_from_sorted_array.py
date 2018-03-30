# 26. Remove Duplicates from Sorted Array
# Python 3
# https://leetcode.com/problems/remove-duplicates-from-sorted-array

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums[:] = sorted(set(nums))
    return len(nums)

nums = [1, 1, 2]
print('Length: {} | Array: {}'.format(removeDuplicates(nums), nums))