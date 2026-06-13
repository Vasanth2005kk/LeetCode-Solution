from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if nums[i] ==  target:
                output.append(i)

        return output

nums = [1,2,5,2,3]
target = 2
obj = Solution().targetIndices(nums,target)

print(obj)