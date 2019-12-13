#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
# https://leetcode-cn.com/problems/task-scheduler/description/
#
# algorithms
# Medium (45.77%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 21.1K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26
# 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
# 
# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
# 
# 你需要计算完成所有任务所需要的最短时间。
# 
# 示例 1：
# 
# 
# 输入: tasks = ["A","A","A","B","B","B"], n = 2
# 输出: 8
# 执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
# 
# 
# 注：
# 
# 
# 任务的总个数为 [1, 10000]。
# n 的取值范围为 [0, 100]。
# 
# 
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        curr_quene = [] ## 过去n时间内的操作
        ans = 0
        while tasks:
            for i in tasks:
                if i not in curr_quene:
                    ans += 1
                    curr_quene.append(i)
                    tasks.remove(i)
                    if len(curr_quene) > n:
                        curr_quene.pop(0)
                    print(i, ans, curr_quene, tasks)
                    
            if not tasks:
                break
            while len(curr_quene) <= n:
                if len(curr_quene)==n and 0 in curr_quene:
                    break
                curr_quene.append(0)
                ans += 1
                if len(curr_quene)==n+1:
                    curr_quene.pop(0)
                    break

        return ans
# @lc code=end

