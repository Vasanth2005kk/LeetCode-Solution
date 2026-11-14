from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        postive = 0
        nagtive = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                print(nums[i])
                postive += nums[i]
            else:
                nagtive -= nums[i]

        print(postive,nagtive)
        return postive + nagtive

nums = [1,3,5,7]
obj = Solution().alternatingSum(nums)

print(obj)