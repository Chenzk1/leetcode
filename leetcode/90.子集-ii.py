#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def help1(index, temp):
            if temp not in ans:
                ans.append(temp)
            for i in range(index,n):
                help1(i+1, temp+[nums[i]])

        def help2(index, temp):
            ans.append(temp)
            for i in range(index,n):
                if i > index and nums[i]==nums[i-1]:
                    continue
                help2(i+1, temp+[nums[i]])

        help1(0, [])
        return ans



# @lc code=end

