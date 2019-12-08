#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (59.89%)
# Likes:    327
# Dislikes: 0
# Total Accepted:    62.1K
# Total Submissions: 103.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ## 有递归写法 更简单
        if not root:
            return []
        quene = []
        ans = []
        quene.append(root)
        while quene:
            tmp1 = []
            tmp2 = []
            while quene:
                node = quene.pop(0)
                if node.left:
                    tmp2.append(node.left)
                if node.right:
                    tmp2.append(node.right)
                tmp1.append(node.val)
            quene = tmp2
            ans.append(tmp1)
        return ans


# @lc code=end

