# encoding=utf-8
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x<0: return False
        # if str(x)[::-1] == str(x): return True
        # else: return False

        if x<0 or ( not x%10 and x!=0): return False
        half_back = 0
        while half_back < x:
            half_back = half_back*10 + x%10
            x //= 10
        return (x==half_back) or (x==(half_back//10))
        
# @lc code=end

Solution().isPalindrome(121)