#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (38.23%)
# Likes:    173
# Dislikes: 0
# Total Accepted:    16.7K
# Total Submissions: 43.5K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        if endWord not in wordList:
            return 0
        
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                wordDict[word[:i]+'*'+word[i+1:]].append(word)

        quene = [(beginWord,1)]
        visited = [beginWord]
        while quene:
            curWord, level = quene.pop(0)
            for i in range(len(beginWord)):
                tmp = curWord[:i] + "*" + curWord[i+1:]
                for word in wordDict[tmp]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited.append(word) # 每次都是同一层，因此之后继续遍历的时候就没必要再回到这一层的某个节点了，
                        # 如果再回来只会更远，所以这里visited是可以的
                        quene.append((word, level+1))
                wordDict[tmp] = []

        return 0
        
# @lc code=end

