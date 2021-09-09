# encoding=utf-8
#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ## 快慢指针
        def half_end(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def recursive_last_half(head):
            prev = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        if not head or not head.next:
            return True
        prev_half_end = half_end(head)
        last_half_begin = recursive_last_half(prev_half_end.next)
        while last_half_begin:
            if head.val != last_half_begin.val:
                return False
            head = head.next
            last_half_begin = last_half_begin.next
            # if head != prev_half_end: break
        return True
        
# # @lc code=end
# a = ListNode(1)
# b = ListNode(1)
# c = ListNode(2)
# d = ListNode(1)
# a.next = b
# b.next = c
# c.next = d
# Solution().isPalindrome(a)