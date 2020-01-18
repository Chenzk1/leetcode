#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#
# https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/description/
#
# algorithms
# Easy (59.84%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 12.2K
# Testcase Example:  '"this apple is sweet"\n"this apple is sour"'
#
# 给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
# 
# 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
# 
# 返回所有不常用单词的列表。
# 
# 您可以按任何顺序返回列表。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet","sour"]
# 
# 
# 示例 2：
# 
# 输入：A = "apple apple", B = "banana"
# 输出：["banana"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A 和 B 都只包含空格和小写字母。
# 
# 
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        all_ = A.split(" ") + B.split(" ")
        d = {}
        ans = []
        for i in all_:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if d[i] == 1:
                ans.append(i)
        return ans

# @lc code=end

