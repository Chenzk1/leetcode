#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = postorder[-1]
        idx = inorder.index(root)
        rootNode = TreeNode(root)
        rootNode.left = self.buildTree(inorder[:idx], postorder[:idx])
        rootNode.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return rootNode

# @lc code=end

