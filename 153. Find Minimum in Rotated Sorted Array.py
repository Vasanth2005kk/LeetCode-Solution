class Solution:
    def findMin(self, nums: list[int]) -> int:
        return min(nums)


nums = [3,4,5,1,2]
obj= Solution().findMin(nums)
print(obj)