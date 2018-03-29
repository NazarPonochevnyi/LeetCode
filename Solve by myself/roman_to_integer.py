# 13. Roman to Integer
# Python 3
# https://leetcode.com/problems/roman-to-integer

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    tranform = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }
    result, prev_number = 0, 0
    for symbol in reversed(s):
        number = tranform[symbol]
        if number >= prev_number:
            result += number
        else:
            result -= number
        prev_number = number
    return result

roman = 'MDMCLXIIX'
print(romanToInt(roman))