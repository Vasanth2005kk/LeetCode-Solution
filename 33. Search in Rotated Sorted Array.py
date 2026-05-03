from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:  

        iindex = 0
        dindex = -1
        numLength = len(nums)

        while iindex < numLength:

            if nums[iindex] == target:
                return iindex

            if nums[dindex] == target:
                return numLength + dindex

            iindex += 1
            dindex -= 1

        return -1


nums = [4,5,6,7,0,1,2]
target = 0

obj = Solution().search(nums,target)
print(obj)