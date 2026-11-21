class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        output = []
        for i in range(len(nums)):
            total += nums[i]
            output.append(total)

        return output



nums = [1, 2, 3, 4]
nums = [1, 1, 1, 1, 1]
nums = [3, 1, 2, 10, 1]

obj = Solution().runningSum(nums)
print(obj)