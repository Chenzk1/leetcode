#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n<4:
            return []
        ans = []
        print(nums)
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if nums[i]+nums[n-1]+nums[n-2]+nums[n-3]<target:
                    break
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:
                    break
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k = j+1
                m = n-1
                print(i,j,k,m)
                while k<m:
                    t = nums[i]+nums[j]+nums[k]+nums[m]
                    if t==target:
                        ans.append([nums[i], nums[j], nums[k], nums[m]])
                        while k<m and nums[k]==nums[k+1]:
                            k+=1
                        while k<m and nums[m]==nums[m-1]:
                            m-=1
                        k+=1
                        m-=1
                    if t < target:
                        k+=1
                    if t > target:
                        m-=1
                    
        return ans
# @lc code=end

