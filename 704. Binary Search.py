from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        arrlength = len(nums)

        left = 0
        right = arrlength-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
nums = [-1,0,3,5,9,12]
target = 9

obj = Solution().search(nums,target)

print(obj)