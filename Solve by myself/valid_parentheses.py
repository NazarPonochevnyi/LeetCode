# 20. Valid Parentheses
# Python 3
# https://leetcode.com/problems/valid-parentheses

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    wait = []
    opened, closed = ['(', '[', '{'], [')', ']', '}']
    transform = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in opened:
            wait.append(transform[char])
            continue
        if char in closed:
            if wait:
                if wait[-1] == char:
                    del wait[-1]
                    continue
                return False
            return False
    return True if not wait else False

string = '({Hello, World!)}'
print(isValid(string))