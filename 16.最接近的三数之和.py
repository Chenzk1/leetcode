#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        m = target - (nums[0]+nums[1]+nums[2])
        nums.sort()
        for i in range(n-2):
            if i>=3 and nums[i-3]>=target:
                break
            # if i+3<n and nums[i+3]<=target:
            #     continue
            j=i+1
            k=n-1
            while j<k:
                temp = target - (nums[i]+nums[j]+nums[k])
                if abs(temp) < abs(m):
                    m = temp
                if temp==0:
                    return target
                elif temp>0:
                    j += 1
                elif temp<0:
                    k -= 1
        return target-m        
# @lc code=end

