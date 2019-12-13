#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = preorder[0]
        idx = inorder.index(root)
        rootNode = TreeNode(root)
        rootNode.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        rootNode.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return rootNode

# @lc code=end

