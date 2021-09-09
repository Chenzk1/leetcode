#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode()
        tail = head
        carry = 0
        while l1 or l2:
            left = l1.val if l1 else 0
            right = l2.val if l2 else 0
            sum_ = left + right + carry
            carry = sum_ // 10
            value = sum_ % 10
            cur = ListNode(value)
            tail.next = cur
            tail = tail.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            tail.next = ListNode(carry)
        return head.next
# @lc code=end

