#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # if not head.next:
        #     return None
        # nums = 0
        # cur = head
        # while cur:
        #     cur = cur.next
        #     nums += 1
        # if nums == n:
        #     return head.next
        # else:
        #     cur = head
        #     for i in range(nums-n-1):
        #         cur = cur.next
        #         print(cur.val)
        #     cur.next = cur.next.next
        #     return head

        if not head.next:
            return None
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        if n == len(nodes):
            return nodes[1] if n!=1 else None
        else:
            nodes[-1-n].next = nodes[-n].next
            return nodes[0]

# @lc code=end
