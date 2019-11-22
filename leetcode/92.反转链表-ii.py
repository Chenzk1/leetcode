#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n==1 or head==None or head.next==None:
            return head
        stop = False
        left, right = head, head
        def help(m, n, right):# right 作为每轮迭代的变量，避免了链表无法倒序的问题
            nonlocal left,stop ## 要么声明全局变量
            if n == 1:
                return

            right = right.next
            if m>1:
                left = left.next
            help(m-1, n-1, right)
            print(left.val, right.val, m, n)
            if left==right or left==right.next:
                stop=True
            if not stop:# ~False = -2
                left.val, right.val = right.val, left.val
                left = left.next
            return
        help(m, n, right)
        return head
# @lc code=end

