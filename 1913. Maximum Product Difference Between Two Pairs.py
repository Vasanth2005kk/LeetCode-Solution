from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # print(nums)
        a , b , c , d = nums[0] , nums[1] , nums[-1] , nums[-2]
        # print(a,b,c,d)
        return (c*d) - (a*b)

nums = [4,2,5,9,7,4,8]

obj = Solution().maxProductDifference(nums)

print(obj)