#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (48.58%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    19.1K
# Total Submissions: 39.3K
# Testcase Example:  '2\n[[1,0]]'
#
# 现在你总共有 n 门课需要选，记为 0 到 n-1。
# 
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
# 
# 给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
# 
# 示例 1:
# 
# 输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 
# 示例 2:
# 
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
# 
# 说明:
# 
# 
# 输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 
# 
# 提示:
# 
# 
# 这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
# 通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
# 
# 拓扑排序也可以通过 BFS 完成。
# 
# 
# 
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        广度优先
        入度表：每个节点需要的前置节点数量
        领接表：每个节点的后序节点列表
        一个队列：存放可以安排的课程，即无前置节点的节点
        '''
        # inDegree = [0 for _ in range(numCourses)]
        # adjList = [[] for _ in range(numCourses)]
        # for pre, cur in prerequisites:
        #     inDegree[cur] += 1
        #     adjList[pre].append(cur)
        # quene = []
        # ## 不需要前置即入度为1的节点入队
        # for i in range(numCourses):
        #     if inDegree[i]==0:
        #         quene.append(i)
        
        # while quene:
        #     cur = quene.pop(0)
        #     # 每出队一个相当于安排了一门课程
        #     numCourses -= 1
        #     # 此节点为前序节点的所有节点入度-1，如果入度为0的，入队
        #     for i in adjList[cur]:
        #         inDegree[i] -= 1
        #         if not inDegree[i]:
        #             quene.append(i)
        # # 队列为空的时候，说明没有节点可以安排；若此时还有课程未安排，说明有问题
        # return not numCourses
        '''
        深度优先
        对每个节点做深度优先遍历
        flags: -1: 被其他节点启动的DFS访问过；0：未被访问；1：被自己启动的DFS访问过
        '''
        def dfs(i, adjList):
            # 该节点已经被其他节点启动的DFS遍历过，返回True
            if flags[i]==-1:
                return True
            # 已经被自己启动的DFS访问过，说明有环
            if flags[i]==1:
                return False
            flags[i] = 1 # 标记，如果下面这个循环里的dfs又遍历到了i，则说明有环
            for j in adjList[i]:
                if not dfs(j, adjList):
                    return False
            flags[i] = -1 # 此节点没问题，之后不需要再遍历了
            return True

        adjList = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for pre, cur in prerequisites:
            adjList[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjList):
                return False
        return True

# @lc code=end

