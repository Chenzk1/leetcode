#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        题目的意思是 比如12345 6543 找出比这个序列更大的序列中最小的序列12346 3455
        为了保持最小的序列 从右往左遍历 保证左边一致
        为了保证更大 即只要找到一个nums[i] > nums[i-1]即可 i之后的为 降序
        （为了保持最小 即i之后的最小的大于num[i-1]的数 要移到i-1处 所以要相邻）
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,i,j):
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            return nums
        n = len(nums)
        index1 = -1
        for i in range(n-2,-1,-1):
            if nums[i+1] > nums[i]:
                index1 = i
                break
        if index1 == -1:
            nums = reverse(nums,0,n-1)
            return
        index2 = -1
        for j in range(n-1,i,-1):
            if nums[j]>nums[i]:
                index2 = j
                break
        nums[index1],nums[index2] = nums[index2],nums[index1]
        nums = reverse(nums,index1+1,n-1)
# @lc code=end

