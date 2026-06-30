from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}

        for value in nums:
            if value not in dic:
                dic[value] = 1
            else:
                if dic[value] == 1:
                    dic[value] +=1
                else:
                    del dic[value]
        return list(dic.keys())[0]


nums = [0,1,0,1,0,1,99]
obj = Solution().singleNumber(nums)

print(obj)
