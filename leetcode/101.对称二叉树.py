#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (49.12%)
# Likes:    527
# Dislikes: 0
# Total Accepted:    74.7K
# Total Submissions: 152K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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
    def isSymmetric(self, root: TreeNode) -> bool:
        ## 递归
        # def help(left, right):
        #     if not left and not right:
        #         return True
        #     if not (left and right):
        #         return False
        #     if left.val != right.val:
        #         return False
        #     return help(left.left, right.right) and help(left.right, right.left)
        
        # return help(root.left, root.right) if root else True

        ## 迭代 调整入队列的方式
        quene = []
        quene +=[root, root]
        while quene:
            q1 = quene.pop()
            q2 = quene.pop()
            if not q1 and not q2:
                continue
            if not (q1 and q2):
                return False
            if q1.val != q2.val:
                return False
            quene.append(q1.left)
            quene.append(q2.right)
            quene.append(q1.right)
            quene.append(q2.left)
        return True


# @lc code=end

