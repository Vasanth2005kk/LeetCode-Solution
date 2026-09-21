class Solution:
    def findDisappearedNumbers(self, nums):
        num_set = set(nums)  
        output = []
                
        for i in range(1, len(nums) + 1):
            if i not in num_set:
                output.append(i)
        return output


nums = [4,3,2,7,8,2,3,1]
obj = Solution().findDisappearedNumbers(nums)

print(obj)