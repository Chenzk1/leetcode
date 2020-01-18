#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (46.05%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 23.3K
# Testcase Example:  '[1,3,5]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
# 
# 请找出其中最小的元素。
# 
# 注意数组中可能存在重复的元素。
# 
# 示例 1：
# 
# 输入: [1,3,5]
# 输出: 1
# 
# 示例 2：
# 
# 输入: [2,2,2,0,1]
# 输出: 0
# 
# 说明：
# 
# 
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
# 
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return
        elif n == 1:
            return nums[0]
        mid = n // 2 # 2: 1; 3: 1; 4: 2
        if nums[0] > nums[mid-1]:
            return self.findMin(nums[:mid])
        elif nums[mid] > nums[-1]:
            return self.findMin(nums[mid:])
        elif nums[0] == nums[mid-1] or nums[mid] == nums[-1]:
            return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))
        else:
            return min(nums[0],nums[mid]) 
        ## 题解更清晰

# @lc code=end

