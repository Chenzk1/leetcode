#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# https://leetcode-cn.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (61.66%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    16K
# Total Submissions: 26K
# Testcase Example:  '[4,2,1,3]'
#
# 对链表进行插入排序。
# 
# 
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
# 
# 
# 
# 插入排序算法：
# 
# 
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 
# 
# 
# 
# 示例 1：
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2：
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
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
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
     	# 找个排头 方便之后判断pre.next 如果用pre判断的话无法插入; 另外方便之后返回头
        pre = dummy = ListNode(-1)
        cur = head
        while cur:
            tmp = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = tmp
        return dummy.next
        

# @lc code=end

