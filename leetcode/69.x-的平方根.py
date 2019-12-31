#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        left, right = 0, (x+1)//2
        while left < right:
            mid = (left+right)//2 + 1
            if mid**2 > x:
                right = mid-1
            else:
                left = mid

        return left
        
# @lc code=end

