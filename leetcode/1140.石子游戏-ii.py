#
# @lc app=leetcode.cn id=1140 lang=python3
#
# [1140] 石子游戏 II
#

# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sum_from_end = [0]*n
        for i in range(n-1,-1,-1):
            sum_from_end[i] = sum(piles[i:])
        dp = dict() # 避免二次搜索，这里使用字典是因为如果用数组的话有些元素用不到，造成空间复杂度过高
        def helper(i, M):
            if (i, M) in dp:
                return dp[(i, M)]
            if i >= n:
                return 0
            if i+2*M >= n:
                return sum_from_end[i]
            best = 0
            for j in range(i+1, i+2*M+1): # 遍历
                best = max(best, sum_from_end[i] - helper(j, max(M, j-i))) # 另一位也要发挥最高水平
            dp[(i, M)] = best
            return best

        return helper(0, 1)
# @lc code=end

