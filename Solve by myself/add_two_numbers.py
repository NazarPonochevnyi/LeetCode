# 2. Add Two Numbers
# Python 3
# https://leetcode.com/problems/add-two-numbers

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    next_add = 0
    header = l1
    currnt = None
    while l1 and l2:
        temp_sum = l1.val + l2.val + next_add
        l1.val = temp_sum % 10
        next_add = temp_sum / 10
        currnt = l1
        l1 = l1.next
        l2 = l2.next

        if l2:
            currnt.next = l2

        while next_add:
            if not currnt.next:
                currnt.next = ListNode(next_add)
                return header
            else:
                currnt = currnt.next
                temp_sum = currnt.val + next_add
                currnt.val = temp_sum % 10
                next_add = temp_sum / 10

        return header