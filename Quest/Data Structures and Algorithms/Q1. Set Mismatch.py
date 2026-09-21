from typing import List , Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        output = [0,0]

        for i in range(1, len(nums)+1):
            if count[i] == 2:
                output[0] = i 
            if count[i] == 0:
                output[1] = i 

        print(output)

        return output       

nums = [1,2,2,4]
obj = Solution().findErrorNums(nums)

print(obj)

