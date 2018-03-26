# 7. Reverse Integer
# Python 3
# https://leetcode.com/problems/reverse-integer

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    result = 0
    s_x = str(x)
    len_x, minus = len(s_x), s_x[0] == '-'
    n = len_x - 1 if not minus else len_x - 2
    if not minus:
        for i in range(len_x - 1, -1, -1):
            result += int(s_x[i]) * pow(10, n)
            n -= 1
        return result if result < 2147483647 else 0
    else:
        for i in range(len_x - 1, 0, -1):
            result += int(s_x[i]) * pow(10, n)
            n -= 1
        return -1 * result if result < 2147483647 else 0

number = -123
print(reverse(number))