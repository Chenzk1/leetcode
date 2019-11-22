#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # ## 用hash
        # d = []
        # while head!=None:
        #     if head in d:
        #         return head
        #     d.append(head)
        #     head = head.next

        # return None
        ## 快慢指针
        if not head or not head.next:
            return None
        slow, fast = head, head
        while True:
            if fast==None or fast.next==None:
                return None
            slow, fast = slow.next, fast.next.next
            if slow==fast:
                break
        fast = head
        while fast!=slow:
            fast, slow = fast.next, slow.next
        return fast


# @lc code=end

