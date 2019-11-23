#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        一次移一位，移k次
        O(k%n * n)
        '''
        # if head == None or head.next == None:
        #     return head
        # if k == 1:
        #     start = head
        #     while start.next!=None:
        #         if start.next.next == None:
        #             new_head = start.next
        #             new_head.next = head
        #             start.next = None
        #             break
        #         else:
        #             start = start.next
        #     return new_head
                        
        # start = head
        # i = 0
        # while start!=None:
        #     start = start.next
        #     i += 1
        # k %= i
        # for _ in range(k):
        #     head = self.rotateRight(head, 1)
        # return head
        '''
        环形链表：先成环，再找开始节点与结尾节点，并断开
        '''
        if not head or not head.next:
            return head
        start = head
        n = 0
        while start!=None:
            n += 1
            if start.next == None:
                start.next = head
                break
            start=start.next
        start = head
        for i in range(n - k%n - 1):
            start = start.next
        new_head = start.next
        start.next = None
        return new_head

# @lc code=end

