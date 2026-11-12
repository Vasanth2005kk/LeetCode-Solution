
from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        inc = 1
        dec = 1
        result = 1

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1

            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1

            else:
                inc = 1
                dec = 1

            result = max(result, inc, dec)

        return result


nums = [1, 4, 3, 3, 2]

obj = Solution()
print(obj.longestMonotonicSubarray(nums))
