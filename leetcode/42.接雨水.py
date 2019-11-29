#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (47.16%)
# Likes:    694
# Dislikes: 0
# Total Accepted:    39.2K
# Total Submissions: 83.2K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        ## 简单 时间：O(n) 空间：O(n)
        # ans = 0
        # h1 = 0
        # h2 = 0
        # n = len(height)
        # if n<3:
        #     return 0
        # for i in range(1,n-1):
        #     h1 = max(height[:i+1])
        #     h2 = max(height[i:])
        #     temp = min(h1,h2)
        #     ans += temp - height[i]

        # return ans
        ## 优化空间复杂度
        ## 要点：只需要考虑左边最大值和右边最大值中较小的一个
        ## 并不从第一个节点计算到第n-1个，而是左右开弓，例如对于左边的，当leftmax大于它，且right也大于它的时候，加之
        ## 左右开弓保证了每次能获得该点左右最大值中的较小值
        ans = 0
        n = len(height)
        if n<3:
            return 0
        left, right = 0, n-1
        left_max, right_max = height[left], height[right]
        while left<right:
            if height[left] < height[right]: ## 这里相当于对左边和右边的最大值的大小做了判断
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else: ## 这里相当于对左边和右边的最大值的大小做了判断
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
        ## 
        # ans = 0
        # h1 = 0
        # h2 = 0
        # for i in range(len(height)):
        #     h1 = max(h1,height[i])
        #     h2 = max(h2,height[-i-1])
        #     ans = ans + h1 + h2 -height[i]
        # return  ans - len(height)*h1

# @lc code=end

