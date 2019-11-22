#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1==None:
        #     return l2
        # elif l2==None:
        #     return l1
        # elif l1.val > l2.val:
        #     l1,l2 = l2,l1
        # head = l1
        # while l1.next!=None and l2!=None:
        #     if l2.val <= l1.next.val:
        #         temp = l1.next
        #         temp1 = l2.next
        #         l1.next = l2
        #         l2.next = temp
        #         l2 = temp1
        #     temp = l1
        #     l1 = l1.next
        # if l1.next == None and l2!=None:
        #     l1.next=l2
        
        # return head

        ## 迭代
        if l1==None:
            return l2
        elif l2==None:
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
# @lc code=end

