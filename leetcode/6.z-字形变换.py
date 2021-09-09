# encoding=utf-8
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:
            return s
        rows = [""] * numRows
        goDown = False
        cur_row = 0
        for cur_s in s:
            rows[cur_row] += cur_s
            if cur_row==0 or cur_row==numRows-1: goDown = not goDown
            cur_row += 1 if goDown else -1
        res = "".join(rows)
        return res


# @lc code=end

# Solution().convert("PAYPALISHIRING", 3)