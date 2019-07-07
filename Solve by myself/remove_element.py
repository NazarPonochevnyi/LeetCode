# 27. Remove Element
# Python 3
# https://leetcode.com/problems/remove-element

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
        
    nums[:] = [num for num in nums if num != val]
    return len(nums)

numbers, value = [3, 2, 2, 3], 3
print('Length: {} | Array: {}'.format(removeElement(numbers, value), numbers))