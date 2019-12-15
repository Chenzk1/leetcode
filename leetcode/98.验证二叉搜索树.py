#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.93%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    53.1K
# Total Submissions: 190.1K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        不只看左右节点，要看左右节点的上下界
        上下界在迭代的时候可以分别由当前节点确定
        '''
        # if not root:
        #     ans = 1
        # elif not (root.left or root.right):
        #     ans = 1
        # elif not root.left:
        #     ans = root.val < root.right.val and self.isValidBST(root.right)
        # elif not root.right:
        #     ans = root.val > root.left.val and self.isValidBST(root.left)
        # else:
        #     ans = root.val < root.right.val and root.val > root.left.val and self.isValidBST(root.left) and self.isValidBST(root.right)
        # return ans    
        ## 迭代
        # def helper(node, lower=float('-inf'), upper=float('inf')):
        #     if not node:
        #         return True
        #     if node.val <= lower or node.val >= upper:
        #         return False
        #     if not helper(node.left, lower, node.val):
        #         return False
        #     if not helper(node.right, node.val, upper):
        #         return False
        #     return True
        
        # return helper(root)
        ## 递归 利用栈
        if not root:
            return True
        stack = []
        stack.append((root, float('-inf'), float('inf')))
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            if root.val <= lower or root.val >= upper:
                return False
            stack.append((root.left, lower, root.val))
            stack.append((root.right, root.val, upper))
        return True
            
# @lc code=end

