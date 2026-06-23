from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
                
        LengthNum = len(nums)
        negativeNumber = 0
        zero = 0

        for i in nums:
            if i == 0:
                zero +=1
            elif i < 0 :
                negativeNumber +=1
            else:
                break
            
        postiveNumber =  LengthNum - negativeNumber - zero

        if postiveNumber >= negativeNumber:
            return postiveNumber
        else:
            return negativeNumber


nums = [-3,-2,-1,0,0,1,2]

obj =  Solution().maximumCount(nums)
print(obj)