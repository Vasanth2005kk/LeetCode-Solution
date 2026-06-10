from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(1,length):
                if i < j < length and (nums[i]+nums[j]) < target:
                    count +=1
        return count
    
nums = [9,-5,-5,5,-5,-4,-6,6,-6]
target = 2

obj = Solution().countPairs(nums,target)
print(obj)