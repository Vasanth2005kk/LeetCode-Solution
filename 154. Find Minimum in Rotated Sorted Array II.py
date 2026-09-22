class Solution:
    def findMin(self, nums: list[int]) -> int:
        return min(nums)


nums = [1,3,5]

obj = Solution().findMin(nums)
print(obj)