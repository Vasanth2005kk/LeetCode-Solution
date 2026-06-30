from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}

        for value in nums:
            if value not in dic:
                dic[value] = 1
            else:
                if dic[value] == 1:
                    del dic[value]

        return list(dic)


nums = [1,2,1,3,2,5]
obj = Solution().singleNumber(nums)

print(obj)