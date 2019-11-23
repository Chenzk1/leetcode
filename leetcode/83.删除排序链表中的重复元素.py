#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cache = []
        prev = new_head = ListNode(-1)
        while head != None:
            if head.val not in cache:
                cache.append(head.val)
                prev.next = head
                prev = prev.next
            head = head.next
        prev.next = None ## 注意结尾条件

        return new_head.next
# @lc code=end

