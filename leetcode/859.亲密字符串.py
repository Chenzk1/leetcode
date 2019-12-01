#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# https://leetcode-cn.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.25%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    7.4K
# Total Submissions: 27.3K
# Testcase Example:  '"ab"\n"ba"'
#
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false
# 。
# 
# 
# 
# 示例 1：
# 
# 输入： A = "ab", B = "ba"
# 输出： true
# 
# 
# 示例 2：
# 
# 输入： A = "ab", B = "ab"
# 输出： false
# 
# 
# 示例 3:
# 
# 输入： A = "aa", B = "aa"
# 输出： true
# 
# 
# 示例 4：
# 
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
# 
# 
# 示例 5：
# 
# 输入： A = "", B = "aa"
# 输出： false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A 和 B 仅由小写字母构成。
# 
# 
#

# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        m = len(A)
        n = len(B)
        if m<2 and m!=n:
            return False
        tmp = []
        for i in range(m):
            if A[i]!=B[i]:
                tmp.append(i)
                if len(tmp)>2:
                    return False
        if len(tmp)==0 and len(set(A))<m:
            return True
        elif len(tmp)==2 and A[tmp[0]]==B[tmp[1]] and A[tmp[1]]==B[tmp[0]]:
            return True
        else:
            return False

# @lc code=end

