
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n =  len(nums)

        for i in range(n-1,-1,-1):
            nums.append(nums[i])
        return nums

nums = [1,2,3]


obj = Solution().concatWithReverse(nums)

print(obj)