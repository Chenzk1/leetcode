#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ## 递归
        # if root == None:
        #     return []
        # ans = []
        # ans.append(root.val)
        # ans += self.preorderTraversal(root.left)
        # ans += self.preorderTraversal(root.right)
        # return ans
        ## 迭代
        if root == None:
            return []
        ans = []
        stack = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            if curr:
                ans.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return ans

        
# @lc code=end

