#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in mapping:
                top = stack.pop() if stack else '-1'
                if mapping[i]!=top:
                    return False
            else:
                stack.append(i)
            
        return not stack
        
# @lc code=end

