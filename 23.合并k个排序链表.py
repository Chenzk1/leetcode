#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (47.86%)
# Likes:    391
# Dislikes: 0
# Total Accepted:    56K
# Total Submissions: 117.1K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        暴力法 k个链表，N个节点
        O(k) + O(kN)
        '''
        # if len(lists)==0:
        #     return None
        # head = start = ListNode(-1)
        # cache = []
        # for i in lists:
        #     if i!=None:
        #         cache.append(i)
        
        # while cache!=[]:
        #     min_node = cache[0]
        #     for i in cache:
        #         if i==None:
        #             contine
        #         elif i.val < min_node.val:
        #             min_node = i
            
        #     start.next = min_node
        #     start = start.next
        #     cache.remove(min_node)
        #     if min_node.next!=None:
        #         cache.append(min_node.next)
        # return head.next
        
        '''
        分治法
        O(Nlogk)
        '''
        def merge2Lists(l1, l2) -> ListNode:
            head = start = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    start.next = l1
                    l1 = l1.next
                else:
                    start.next = l2
                    l2 = l2.next
                start = start.next
                
            if l1!=None:
                start.next = l1
            elif l2!=None:
                start.next = l2
            return head.next
        
        interval = 1
        n = len(lists)

        while interval < n:
            for i in range(0, n-interval, interval*2):
                lists[i] = merge2Lists(lists[i], lists[i+interval])
            interval *= 2

        return lists[0] if n>0 else None

# @lc code=end

