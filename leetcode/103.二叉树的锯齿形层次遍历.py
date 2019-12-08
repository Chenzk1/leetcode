#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (52.72%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    24.7K
# Total Submissions: 46.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层次遍历如下：
# 
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return []
        def help(node, level):
            if level==len(ans):
                ans.append([])
                
            if level%2==0:
                ans[level].append(node.val)
            else:
                ans[level].insert(0,node.val)

            if node.left:
                help(node.left, level+1)
            if node.right:
                help(node.right, level+1)
        

        help(root, 0)
        return ans
# @lc code=end

