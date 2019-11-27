#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = [] # 使用辅助栈而不用一个变量的原因是，最小值会不断变化
        
    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        # else:
        #     self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            ans = self.data.pop()
            if self.helper and self.helper[-1] == ans:
                self.helper.pop()
            return ans

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

