from  typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positive = set(x for x in nums if x > 0)

        if positive:
            return sum(positive)

        return max(nums)


nums = [2,-10,6]

obj = Solution().maxSum(nums)

print(obj)