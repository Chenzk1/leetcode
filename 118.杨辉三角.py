#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        ans = [[1]]
        for i in range(1,numRows):
            temp=[1]
            for j in range(1,len(ans[i-1])):
                temp.append(ans[i-1][j-1]+ans[i-1][j])
            temp.append(1)
            ans.append(temp)
        return ans


# @lc code=end

