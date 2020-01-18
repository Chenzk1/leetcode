#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (36.06%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    12.2K
# Total Submissions: 33.9K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 
# 示例 1:
# 
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 
# 
# 示例 2:
# 
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 
# 
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        start = 0
        n = len(intervals)
        while start < n and intervals[start][0] < newInterval[0]:
            ans.append(intervals[start])
            start += 1

        if not ans or ans[-1][1] < newInterval[0]:
            ans.append(newInterval)
        else:
            ans[-1][1] = max(newInterval[1], ans[-1][1])
        
        while start < n:
            if ans[-1][1] < intervals[start][0]:
                ans.append(intervals[start])
            else:
                ans[-1][1] = max(intervals[start][1], ans[-1][1])
            start += 1

        return ans


# @lc code=end

