#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ## 先排序再寻找
        # nums.sort()
        # flag = 0
        # n = len(nums)
        # if n==1:
        #     if nums[0]==1:
        #         return 2
        #     else:
        #         return 1
        # for i in range(n):
        #     print(i, nums[i])
        #     if flag==0 and nums[i]>0:
        #         if nums[i]!=1:
        #             return 1
        #         flag = 1
        #     if nums[i]>0:
        #         if i<=n-2 and nums[i+1]-nums[i]>=2:
        #             return nums[i]+1
        #         elif i>=n-2:
        #             return nums[n-1]+1
        # return 1
        ## 官方题解
        ## 利用原数组的索引和正负号来表示索引值有没有出现
        ## 关键在于结果不会超过n+1，所以只需要看1~n有没有出现即可
        ## 特例 n
        n = len(nums)
        # 要先判断1，否则的话后续填充有问题
        if 1 not in nums:
            return 1

        if n==1:
            return 2

        for i in range(n):
            if nums[i]<1 or nums[i]>n:
                nums[i] = 1
        for i in range(n):
            a = abs(nums[i])
            if a==n:### a==n
                if nums[0]>0:
                    nums[0] = -nums[0]
            elif nums[a]>0:
                nums[a] = -nums[a]

        for i in range(1,n):
            if nums[i] > 0:
                return i
        if nums[0]>0:
            return n
        return n+1
# @lc code=end

