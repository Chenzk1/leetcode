#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n<1:
            return [-1,-1]
        ans = []
        def help(i,j):
            if i==j and nums[i]==target:
                return [i]
            elif nums[i]<=target and nums[j]>=target:
                a = help(i,(i+j)//2)
                b = help((i+j)//2+1,j)
                return a+b

            return []
        ans = help(0,n-1)
        if ans == []:
            return [-1,-1]
        return [min(ans),max(ans)]

               

# @lc code=end

