from typing import List

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:

        n =  len(nums)
        res = 0

        if k == 0:
            return n
        nums.sort()
        threshold = nums[n-k]

        for i in nums:
            if i < threshold:
                res+=1
        
        return res
    
nums = [5,5,5,6,6]
k = 1


obj = Solution().countElements(nums,k)
print(obj)