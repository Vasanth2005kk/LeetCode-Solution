from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dic = {}

        for i in nums:
            if i in dic:
                if dic[i] >= 2:
                    return False
                dic[i] = dic[i]+1
            else:
                dic[i] = 1

        return True



nums = [1,1,1,1]

obj = Solution().isPossibleToSplit(nums)
print(obj)