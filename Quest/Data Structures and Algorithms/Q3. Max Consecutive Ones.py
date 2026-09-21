from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnce = 0

        count = 0
        for i in nums:
            if i == 1:
               count +=1 
            else:
                count = 0

            if maxOnce < count:
                maxOnce = count

        return maxOnce

nums = [1,1,0,1,1,1]

obj = Solution().findMaxConsecutiveOnes(nums)
print(obj)