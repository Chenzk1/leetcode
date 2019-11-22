#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## 递归
        # if nums==[]:
        #     return [[]]
        # n = len(nums)
        # def help(index):
        #     if index==0:
        #         return [[nums[index]], []]
        #     else:
        #         temp = help(index-1)
        #         ans = temp + [[nums[index]] + num for num in temp]
        #         return ans
        # ans = help(n-1)
        # print(ans)
        # return ans 

        ## 迭代
        # ans = [[]]
        # for i in nums:
        #     ans = ans+[[i]+num for num in ans]
        # return ans

        ## 递归 回溯
        res = []
        n = len(nums)

        def helper(index, tmp):# 求取第index~n的元素为首的组合，因为去重，所以j in range(index,n)
            res.append(tmp) ### 每一次迭代的工作是将tmp+[nums[index]]加入数组
            for j in range(index,n):
                helper(j+1, tmp+[nums[j]])

        helper(0, [])
        return res
# @lc code=end

