#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (63.62%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    22.4K
# Total Submissions: 35.3K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 
# 示例:
# 
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
#

# @lc code=start
## 二叉查找树（Binary Search Tree），它或者是一棵空树，或者是具有下列性质的二叉树：
##  若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
## 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
## 它的左、右子树也分别为二叉排序树。
class Solution:
    def numTrees(self, n: int) -> int:
        ## dp O(N^2)
        ## G(0)=1 G(1)=1
        ## G(n)为从1~n作为根节点得到的数量之和，左边为i个数时，右边为n-i-1个数，i的取值为0~n-1
        ## 所以G(n) = G(i)G(n-i-1)
        G = [0]*(n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                G[i] += G[j]*G[i-j-1]
        return G[n]
# @lc code=end

