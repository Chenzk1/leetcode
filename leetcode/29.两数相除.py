#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (19.02%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    30.2K
# Total Submissions: 158.6K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 
# 示例 1:
# 
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 
# 示例 2:
# 
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 
# 说明:
# 
# 
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
# 
# 
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ## 二分法
        if dividend == -2**31 and divisor == -1:
            return 2**31-1

        flag = 1
        if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
            flag = -1
        divisor = abs(divisor)
        dividend = abs(dividend)
        ans = 0

        while divisor <= dividend:
            i = 1
            tmp = divisor
            while tmp+tmp <= dividend:
                tmp += tmp
                i += i
            dividend -= tmp
            ans += i
        return flag*ans
        ## 位运算
        # sign = (dividend > 0) ^ (divisor > 0)
        # dividend = abs(dividend)
        # divisor = abs(divisor)
        # count = 0
        # #把除数不断左移，直到它大于被除数
        # while dividend >= divisor:
        #     count += 1
        #     divisor <<= 1
        # result = 0
        # while count > 0:
        #     count -= 1
        #     divisor >>= 1
        #     if divisor <= dividend:
        #         result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
        #         dividend -= divisor
        # if sign: result = -result
        # return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1 

                
# @lc code=end

