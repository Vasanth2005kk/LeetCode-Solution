class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        if len(nums) == 1:
            nums = sorted(nums[0])
            return nums
        
        
        output =[]
        for i in range(len(nums)-1):
            if not output:
                ans = set(nums[i]).intersection(set(nums[i+1]))
            else:
                ans = set(output).intersection(set(nums[i+1]))
            output.clear()
            output.extend(ans)
            
        output =  sorted(set(output))
        return output

# nums = [[20,25,49],[16,7,20,47,17],[17,20]]
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]


obj = Solution().intersection(nums)
print(obj)