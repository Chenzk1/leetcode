#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # ## hash
        # d = []
        # while head != None:
        #     if head in d:
        #         return True
        #     d.append(head)
        #     head = head.next
        # return False
        ## 快慢指针
        if not head or not head.next :
            return False
        slow,fast = head, head.next
        while fast and fast.next:
            if slow==fast:
                return True
            slow, fast = slow.next, fast.next.next

# @lc code=end

