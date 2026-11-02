from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for i in nums:
            if i % 2 == 0:
                count +=1
            if count == 2:
                return True
        return False

nums = [1,2,3,4,5]
nums = [2,4,8,16]
nums = [1,3,5,7,9]

obj = Solution().hasTrailingZeros(nums)
print(obj)