#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(n)]
        stack = [] # 存放当前需要处理的元素的下表
        double_nums = nums+nums
        for i, num in enumerate(double_nums): ## 遍历一圈
            while stack and nums[stack[-1]] < num: ## 最近的词满足条件则输出；只有上一个词不小于当前词时，才会保留上一个词并压入当前词
                ans[stack[-1]] = num
                stack.pop()
            if i < n:
                stack.append(i)
        return ans
            
# @lc code=end

