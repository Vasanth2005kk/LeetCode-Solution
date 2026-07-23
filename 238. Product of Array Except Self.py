from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ouptut = [1]*len(nums)
        prf = 1

        for i in range(len(nums)):
            ouptut[i] = prf
            prf = prf * nums[i]
        sef = 1
        for j in range(len(nums)-1,-1,-1):
            ouptut[j] = ouptut[j]*sef
            sef = sef*nums[j]
        return ouptut

nums = [1,2,3,4]
obj = Solution().productExceptSelf(nums)
print(obj)


