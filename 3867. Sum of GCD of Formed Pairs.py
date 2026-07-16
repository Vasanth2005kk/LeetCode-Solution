import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        currentMax = 0

        # Construct prefixGcd
        for num in nums:
            currentMax = max(currentMax, num)
            prefixGcd.append(math.gcd(num, currentMax))
        
        # Sort prefixGcd
        prefixGcd.sort()

        # Form pairs and calculate the sum of GCDs
        left = 0
        right = len(prefixGcd) - 1
        total = 0

        while left < right:
            total += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return total

nums = [2,6,4]
obj = Solution().gcdSum(nums)

print(obj)

"""
import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        length = len(nums)

        gcd = []
        index = 0
        for i in range(1,length+1):
            gcd.append(int(math.gcd(nums[index],max(nums[0:i]))))
            index +=1
        # print("Compute prefixGcd :",gcd)
        
        gcd.sort()
        
        # print("Compute prefixGcd Sort:",gcd)
        
        left = 0
        right = len(gcd) - 1
        total =  0
        while left < right:
            gcdValue = math.gcd(gcd[left], gcd[right])  # Pair
            # print(gcdValue)
            total += gcdValue
            left += 1
            right -= 1
        
        return total
"""