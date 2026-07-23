from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastindex = len(nums)-1

        for i in range(lastindex-1,-1,-1):
            if i + nums[i] >= lastindex:
                lastindex = i
        if lastindex == 0:
            return True
        return False



nums = [2,3,1,1,4]

obj = Solution().canJump(nums)
print(obj)

