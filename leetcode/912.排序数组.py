#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        冒泡
        **相邻**两两交换
        O(N^2) 会超时
        优化：从后往前，搞个flag，如果第一次发现已经正序排列，则直接返回，则最好情况可以到O(N)
        '''
        # n = len(nums)
        # for i in range(1,n):
        #     for j in range(i-1,-1,-1):
        #         if nums[j+1] < nums[j]:
        #             nums[j+1],nums[j] = nums[j],nums[j+1]
        # return nums
        '''
        快排
        '''
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        left = [i for i in nums[1:] if i <= pivot]
        right = [i for i in nums[1:] if i > pivot]
        return self.sortArray(left) + [pivot] + self.sortArray(right)

        '''
        插入
        打牌，需要逐个往后挪动
        O(N^2) 会超时
        '''
        # n = len(nums)
        # for i in range(n-1):
        #     pre_index = i
        #     cur_num = nums[i+1]
        #     while pre_index >= 0 and nums[pre_index] > cur_num:
        #         nums[pre_index+1] = nums[pre_index]
        #         pre_index -= 1
        #     nums[pre_index+1] = cur_num

        # return nums
        '''
        shell
        对插入排序的优化
        '''



# @lc code=end

