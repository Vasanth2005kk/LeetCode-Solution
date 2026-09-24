from typing  import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        length = len(nums)
        minValue  = 100
        for index in range(length):
            total = 0
            for num in str(nums[index]):
                total += int(num)
            
            if index == total:
                if minValue > index:
                    minValue = index

        if minValue != 100:
            return minValue

        return -1


nums = [1,10,11]
obj = Solution().smallestIndex(nums)

print(obj)

