#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # prev = new_head = ListNode(-1)
        # flag = 0
        # temp = ListNode(-1)
        # while head!=None:
        #     if head.next!=None:
        #         if (flag == 0 or head.val != temp.val) and head.val != head.next.val:
        #             prev.next = head
        #             prev = prev.next
        #         temp = head
        #         head = head.next
        #     elif flag == 0 or head.val != temp.val:
        #         prev.next = head
        #         prev = prev.next
        #         head = head.next
        #     else:
        #         head = head.next
        #     if flag==0:
        #         flag = 1
        # prev.next = None
        # if new_head==None:
        #     return []
        # return new_head.next
        '''
        以上解法的缺点是需要保留前序节点和后序节点，且比较起来较麻烦
        '''
        thead = ListNode('a')
        thead.next = head
        pre,cur = None,thead
        while cur:
            pre=cur
            cur=cur.next
            while cur and cur.next and cur.next.val == cur.val:
                t=cur.val
                while cur and cur.val==t:
                    cur=cur.next
                pre.next=cur
        return thead.next

# @lc code=end

