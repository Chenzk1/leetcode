#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if i not in ['', '.', '..']:# ''解决了//的问题
                stack.append(i)
            else:
                if i == ".." and stack: # ''和'.'直接跳过
                    stack.pop()
        return '/' + '/'.join(stack)
                
        
# @lc code=end

