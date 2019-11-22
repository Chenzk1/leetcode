#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def combinationSum1(index, target):
            ans = []
            for i in range(index,len(candidates)):
                if candidates[i]==target:
                    ans.append([candidates[i]])
                    break
                if candidates[i]>target:
                    break
                if candidates[i]<target:
                    for j in combinationSum1(i, target-candidates[i]):
                        if j != []:
                            ans.append([candidates[i]]+j)
            return ans
        ans = combinationSum1(0, target)
        return ans


# @lc code=end

