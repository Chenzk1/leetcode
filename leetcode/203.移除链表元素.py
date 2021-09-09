#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        last = dummy
        cur = head
        while cur:
            if cur.val == val:
                last.next = cur.next
            else:
                last = cur
            cur = cur.next
        return dummy.next
# @lc code=end

