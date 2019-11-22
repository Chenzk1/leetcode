#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (44.33%)
# Likes:    298
# Dislikes: 0
# Total Accepted:    23.5K
# Total Submissions: 53K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
# 
# 进阶:
# 
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 示例:
# 
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
# 
# 
#

# @lc code=start

'''
利用原有数据结构OrderedDict实现：需要import以及继承
'''
# from collections import OrderedDict
# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#             self[key] = value
#         else:
#             if len(self) >= self.capacity:
#                 self.popitem(last=False)
#             self[key] = value
'''
用hash实现查询O(1)
用双向链表实现插入删除O(1)
'''
class DLinkList:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
class LRUCache:
    def remove_node(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
    def add_node(self, node):
        start = self.head.next
        
        node.prev = self.head
        node.next = start
        start.prev = node
        self.head.next = node

    def move_to_start(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_end(self, node):
        ans = self.tail.prev
        self.remove_node(self.tail.prev)
        return ans

    
    def __init__(self, capacity: int):
        self.hash = {}
        self.capacity = capacity

        self.size = 0
        self.head = DLinkList()
        self.tail = DLinkList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.hash.get(key,None)
        if not node:
            return -1

        self.move_to_start(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        node = self.hash.get(key)
        if node:
            node.value = value
            self.move_to_start(node)
        else:
            node = DLinkList()
            node.key = key
            node.value = value
            self.hash[key] = node
            
            self.size += 1
            self.add_node(node)
            if self.size > self.capacity:
                tail = self.pop_end(node) ##必须有返回，因为需要pop的跟当前key不一样
                del self.hash[tail.key]
                self.size -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

