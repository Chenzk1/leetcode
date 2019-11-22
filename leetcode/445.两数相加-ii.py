#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (51.76%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 17.4K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
# 
# 
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 进阶:
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 示例:
# 
# 
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b = [], []
        while l1!=None:
            a.append(l1.val)
            l1 = l1.next
        while l2!=None:
            b.append(l2.val)
            l2 = l2.next
        flag = 0
        temp = None
        while a!=[] and b!=[]:
            add = a.pop() + b.pop() + flag
            flag = add//10
            node = ListNode(add%10) ## 当前节点
            node.next = temp ##next指向上一个
            temp = node
        if a==[]:
            a = b
        while a!=[]:
            add = a.pop() + flag
            flag = add//10
            node = ListNode(add%10) ## 当前节点
            node.next = temp ##next指向上一个
            temp = node
        if flag==1:
            node = ListNode(1) 
            node.next = temp
            temp = node
        return temp
# @lc code=end

