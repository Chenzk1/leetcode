#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        m = (j-i) * min(height[i], height[j])
        while i<j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            temp = (j-i) * min(height[i], height[j])
            m = max(temp, m)
        return m
# @lc code=end

