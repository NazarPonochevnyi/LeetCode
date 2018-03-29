# 9. Palindrome Number
# Python 3
# https://leetcode.com/problems/palindrome-number

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    if x < 0: return False
    s_x = str(x)
    len_x = len(s_x)
    for i in range(1, len_x):
        if s_x[i - 1] != s_x[-1 * i]:
            return False
    return True
    
number = -27896532
print(isPalindrome(number))
