#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
# https://leetcode-cn.com/problems/find-peak-element/description/
#
# algorithms
# Medium (43.76%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    24.6K
# Total Submissions: 56.1K
# Testcase Example:  '[1,2,3,1]'
#
# 峰值元素是指其值大于左右相邻值的元素。
# 
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
# 
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
# 
# 你可以假设 nums[-1] = nums[n] = -∞。
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 
# 示例 2:
# 
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5 
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
# 或者返回索引 5， 其峰值元素为 6。
# 
# 
# 说明:
# 
# 你的解法应该是 O(logN) 时间复杂度的。
# 
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def helper(start, end):
            if end - start < 2 or end <= 1 or start >= n-2:
                return 0
            mid = (start + end) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                return helper(start, mid - 1) or helper(mid, end)
            elif nums[mid] > nums[mid+1]:
                return helper(start, mid) or helper(mid+1, end)
            else:
                return helper(start, mid) or helper(mid, end)

        nums = [float('-inf')] + nums + [float('-inf')]
        n = len(nums)
        return helper(0,n-1)-1
# @lc code=end

