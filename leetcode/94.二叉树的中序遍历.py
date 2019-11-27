#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ## 递归
        # if root == None:
        #     return []
        # ans = []
        # ans += self.inorderTraversal(root.left)
        # ans.append(root.val)
        # ans += self.inorderTraversal(root.right)

        # return ans
        ## 迭代
        if root == None:
            return []
        ans = []
        stack = []
        curr = root
        while curr or stack: # curr 不为none则对其作遍历，找left，否则说明其无左右节点，pop
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans
# @lc code=end

