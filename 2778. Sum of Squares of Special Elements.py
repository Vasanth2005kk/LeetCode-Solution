
from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(1,n+1):
            if n % i == 0:
                value = nums[i-1]
                total += value * value

        return total

nums = [2,7,1,19,18,3]
nums = [1,2,3,4]

obj = Solution().sumOfSquares(nums)

print(obj)