#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        O(n2)
        会造成时间超出
        '''
        # if head==None or head.next==None or head.next.next==None:
        #     return head
        # start = head
        # prev = None
        # # find tail node
        # while start!=None:
        #     if start.next == None:
        #         tail = start
        #         break
        #     prev = start
        #     start = start.next
        # prev.next = None
        # tail.next = self.reorderList(head.next)
        # head.next = tail
        # return head
        '''
        先找到序列中点，然后把中点之后的序列反转，然后后面的插到前面
        '''
        if not head or not head.next:
            return head
        start = head
        n = 0
        while start:
            start = start.next
            n += 1
        start, middle = head, head
        j = 0
        while j in range(n//2):
            prev = middle
            middle = middle.next # 0 1 2 middle:1 0 1 middle:1
            j += 1
        middle = self.reverseList(middle)
        prev.next = None

        while middle!=None:
            temp = start.next
            start.next = middle
            middle = middle.next
            if temp:
                start.next.next = temp
            else:
                start.next.next = middle
                break
                
            start = temp

        return
        
# @lc code=end

