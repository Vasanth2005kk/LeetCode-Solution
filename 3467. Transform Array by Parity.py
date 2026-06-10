from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            if i%2 == 0:
                output.append(0)
            else:
                output.append(1)
        output.sort()
        
        return output
    
nums = [4,3,2,1]

obj = Solution().transformArray(nums)

print(obj)