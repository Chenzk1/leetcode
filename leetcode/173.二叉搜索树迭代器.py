#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    ## 能做到O(n)空间复杂度，不符合要求
    # def __init__(self, root: TreeNode):
    #     self.stack = []
    #     self.stack = self.preOrderTraversal(root)
    #     self.stack.sort()
    #     self.stack = self.stack[::-1]

    # def preOrderTraversal(self, root):
    #     ans = []
    #     if root==None:
    #         return ans
    #     ans.append(root.val)
    #     ans += self.preOrderTraversal(root.left)
    #     ans += self.preOrderTraversal(root.right)
    #     return ans

    # def next(self) -> int:
    #     """
    #     @return the next smallest number
    #     """
    #     return self.stack.pop()

    # def hasNext(self) -> bool:
    #     """
    #     @return whether we have a next smallest number
    #     """
    #     return self.stack!=[]
    ## 1. 二叉搜索树：左子树的节点值小于右子树节点值
    ## 2. O(h)时间复杂度，相当于对树的深度做一次遍历 --> 中序遍历
    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_stack(root) #保证栈顶元素最小

    def push_stack(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        ans = self.stack.pop()
        if ans.right:
            self.push_stack(ans.right)
        return ans.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack!=[]
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

