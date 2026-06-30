from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue =  nums[0]
        checking = 0

        for value in nums:
            if checking < 0:
                checking = 0
            checking += value
            if maxValue <= checking:
                maxValue = checking


        return maxValue

nums = [5,4,-1,7,8]
obj = Solution().maxSubArray(nums)

print(obj)
