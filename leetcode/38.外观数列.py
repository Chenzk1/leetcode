#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (53.87%)
# Likes:    372
# Dislikes: 0
# Total Accepted:    66.6K
# Total Submissions: 123.3K
# Testcase Example:  '1'
#
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
# 
# 注意：整数序列中的每一项将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:        
        if n == 1:
            return '1'
        preResult = self.countAndSay(n-1)
        pre = preResult[0]
        count = 1
        ans = []
        for i in range(1, len(preResult)):
            if preResult[i] == pre:
                count += 1
            else:
                ans.append(str(count))
                ans.append(str(pre))
                pre = preResult[i]
                count = 1
        if pre:
            ans.append(str(count))
            ans.append(str(pre))

        return ''.join(ans)
# @lc code=end

