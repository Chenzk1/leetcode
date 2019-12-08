#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (63.25%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 52.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其自底向上的层次遍历为：
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ## 有递归写法 更简单
        ans = []
        quene = []
        if not root:
            return []
        quene.append([root])
        while quene:
            tmp = []
            for node in quene[-1]:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if tmp==[]:
                break
            quene.append(tmp)
        while quene:
            q = quene.pop()
            tmp = []
            for node in q:
                tmp.append(node.val)
            ans.append(tmp)
        return ans

        
# @lc code=end

