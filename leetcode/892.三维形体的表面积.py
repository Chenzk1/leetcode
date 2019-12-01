#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (54.98%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 7.7K
# Testcase Example:  '[[2]]'
#
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
# 
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
# 
# 请你返回最终形体的表面积。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[[2]]
# 输出：10
# 
# 
# 示例 2：
# 
# 输入：[[1,2],[3,4]]
# 输出：34
# 
# 
# 示例 3：
# 
# 输入：[[1,0],[0,2]]
# 输出：16
# 
# 
# 示例 4：
# 
# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
# 
# 
# 示例 5：
# 
# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
# 
# 
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                ele = grid[i][j]
                if ele==0:
                    continue
                tmp = 6*ele - (ele - 1)*2
                if j>0:
                    tmp -= min(grid[i][j-1], ele) * 2
                if i>0:
                    tmp -= min(grid[i-1][j], ele) * 2
                ans += tmp
        return ans


# @lc code=end

