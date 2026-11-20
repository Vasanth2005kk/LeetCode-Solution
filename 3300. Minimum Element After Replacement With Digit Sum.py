from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        values = []

        for i in nums:
            values.append(sum([int(j) for j in str(i)]))

        return min(values)

nums = [10,12,13,14]
obj = Solution().minElement(nums)

print(obj)