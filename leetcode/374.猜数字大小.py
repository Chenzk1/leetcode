#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#
# https://leetcode-cn.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (41.78%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 34.5K
# Testcase Example:  '10\n6'
#
# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
# 
# -1 : 我的数字比较小
# ⁠1 : 我的数字比较大
# ⁠0 : 恭喜！你猜对了！
# 
# 
# 示例 :
# 
# 输入: n = 10, pick = 6
# 输出: 6
# 
#

# @lc code=start
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(1)==0:
            return 1
        if guess(n)==0:
            return n
        left = 1
        right = n

        while left < right:
            mid = (left+right) // 2
            print(left,right,mid)

            tmp = guess(mid)
            if tmp == 0:
                return mid
            elif tmp == 1:
                left = mid
            else:
                right = mid
        
        return left
# @lc code=end

