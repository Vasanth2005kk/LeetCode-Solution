from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        length = len(nums)

        leftSum = []
        rightSum = [None] * length
        left = 0
        right = 0
        revIndex = -1

        for i in range(length):
            leftSum.append(left)
            rightSum[revIndex] = right
            left += nums[i]
            right += nums[revIndex]
            revIndex -=1
        
        output = []
        for j in range(length):
            output.append(abs(leftSum[j] - rightSum[j]))

        return output 

nums = [10, 4, 8, 3]
nums = [1]
obj = Solution().leftRightDifference(nums)

print(obj)