#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ## 递归
        # if root == None:
        #     return []
        # ans = []
        # ans += self.postorderTraversal(root.left)
        # ans += self.postorderTraversal(root.right)
        # ans.append(root.val)

        # return ans
        ## 迭代 左右中 -> 中右左的倒序 只要中间在前，就比较方便
        if root == None:
            return []
        ans = []
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            ans.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return ans[::-1]
# @lc code=end

