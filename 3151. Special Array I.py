from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        length =  len(nums)
        
        if length <= 1:
            return True
        
        start = 0
        end = 1

        while end < length:
            if (nums[start] % 2 == 0 and nums[end] % 2 == 1) or (nums[start] % 2 == 1 and nums[end] % 2 == 0):
                start +=1
                end +=1
            else:
                return False

        return True



nums = [2,1,4]
nums = [4,3,1,6]

obj = Solution().isArraySpecial(nums)

print(obj)