#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (69.40%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    14.6K
# Total Submissions: 21.1K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        '''
        时间复杂度：O(NlogN)。假设链表包含N个元素，对于传入递归函数的每个列表，需要计算它的中间元素。
        对于一个大小为N的链表，需要N/2步找到中间元素。看上去是一个O(N^2)，但仔细分析会发现比O(N^2)更高效。
        N/2 + 2*N/4 + 4*N/8+8*N/16....
        本质是二分查找，所以有logN次
        \begin{aligned} &\sum_{i = 1}^{\log N} 2^{i - 1} \cdot \frac{N}{2^i} \\ = \; &\sum_{i = 1}^{\log N}\frac{N}{2} \\ = \; &\frac{N}{2} \; \log N \\ = \; &O(N\log N) \end{aligned}
        
        空间复杂度：O(logN)。因为使用递归的方法，所以需要考虑递归栈的空间复杂度。对于一棵非平衡二叉树，可能需要O(N)的空间，
        但是问题描述中要求维护一棵平衡二叉树，所以保证树的高度上界为 O(\log N)O(logN)，因此空间复杂度为 O(\log N)O(logN)。
        '''
        if not head:
            return None
        if head.next == None:
            return TreeNode(head.val)
        slow, fast = head, head
        temp = None
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            temp = slow
            slow = slow.next

        if temp:
            temp.next = None
        rootNode = TreeNode(slow.val)
        rootNode.right = self.sortedListToBST(slow.next)
        rootNode.left = self.sortedListToBST(head)
        return rootNode
# @lc code=end

