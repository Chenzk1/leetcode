#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n2 = len(nums2)
        for i in nums1:
            temp = nums2.index(i)
            if temp < n2-1:
                temp1 = [j for j in nums2[temp+1:] if j > i]
                if temp1:
                    ans += [temp1[0]]
                else:
                    ans += [-1]
            else:
                ans += [-1]
        return ans
# @lc code=end

