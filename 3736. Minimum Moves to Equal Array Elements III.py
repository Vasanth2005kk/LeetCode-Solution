from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxValue = max(nums)

        totalMoves = 0
        for i in nums:
            totalMoves +=  maxValue - i 

        print(totalMoves)
        return totalMoves


nums = [2,1,3]
nums = [4,4,5]
obj =  Solution().minMoves(nums)

print(obj)