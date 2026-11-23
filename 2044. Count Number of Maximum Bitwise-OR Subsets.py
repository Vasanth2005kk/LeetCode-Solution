
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        # Find the maximum possible OR
        for num in nums:
            max_or |= num

        count = 0

        def backtrack(index, current_or):
            nonlocal count

            if index == len(nums):
                if current_or == max_or:
                    count += 1
                return

            # Option 1: Include the current element
            backtrack(index + 1, current_or | nums[index])

            # Option 2: Exclude the current element
            backtrack(index + 1, current_or)

        backtrack(0, 0)

        return count


nums = [2,2,2]

obj = Solution().countMaxOrSubsets(nums)