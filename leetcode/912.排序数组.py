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
<<<<<<< HEAD
        快排
        O(NlogN)
=======
        快排1
>>>>>>> 98f06df725b09b6246a74f4390601b0230680e75
        '''
        # if len(nums) <= 1:
        #     return nums
        # pivot = nums[0]
        # left = [i for i in nums[1:] if i <= pivot]
        # right = [i for i in nums[1:] if i > pivot]
        # return self.sortArray(left) + [pivot] + self.sortArray(right)
        '''
        快排2
        '''
        # def help(nums, left, right):
        #     if left >= right:
        #         return
        #     low = left
        #     high = right
        #     pivot = nums[left]
        #     while left < right:
        #         while left < right and nums[right] > pivot:
        #             right -= 1
        #         nums[left] = nums[right]
        #         while left < right and nums[left] <= pivot:
        #             left += 1
        #         nums[right] = nums[left]
        #     nums[right] = pivot
        #     help(nums, low, left-1)
        #     help(nums, right+1, high)
        # help(nums, 0, len(nums)-1)
        # return nums
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
        '''
        归并
        二分递归
        '''
        def merge(left, right):
            result = []
            i=j=0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:] + right[j:]
            return result

        n = len(nums)
        while n<=1:
            return nums
        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return merge(left, right)

# @lc code=end

