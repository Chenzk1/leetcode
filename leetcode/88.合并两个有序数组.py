# -*- coding: UTF-8 -*-
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2
        # nums1.sort()
        i = m-1
        j = n-1
        tail = m+n-1
        while i>=0 or j>=0:
            if i == -1:
                nums1[tail] = nums2[j]
                j -= 1
            elif j == -1:
                nums1[tail] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[tail] = nums2[j]
                j -= 1
            else:
                nums1[tail] = nums1[i]
                i -= 1
            tail -= 1

# @lc code=end

# S = Solution()
# S.merge([1,2,3,0,0,0], 3, [2,5,6], 3)