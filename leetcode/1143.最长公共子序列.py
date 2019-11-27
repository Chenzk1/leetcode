#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ## dp
        m,n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        if m==0 or n==0:
            return 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
        ## 递归 会超时
        # ans = 0
        # if text1=='' or text2=='':
        #     return 0
        # elif text1[-1]==text2[-1]:
        #     ans += self.longestCommonSubsequence(text1[:-1], text2[:-1]) + 1
        # else:
        #     ans += max(self.longestCommonSubsequence(text1[:-1], text2[:]),
        #     self.longestCommonSubsequence(text2[:-1], text1[:]))
        # return ans           

# @lc code=end

