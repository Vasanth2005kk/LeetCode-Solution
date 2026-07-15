"""
class Solution:
    def singleNumber(self, nums) -> int:
        
        if len(nums) == 1:
            return nums[0]
        else:
            d=[]
            check_value=[]

            for i in nums:
                if i in d:
                    check_value.append(i)
                else:
                    d.append(i)

            for i in nums:
                if i not in check_value:
                    return i
"""

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_value = set(nums)
        for i in set_value:
            if nums.count(i) == 1:
                return i
"""
class Solution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
                # print("checking Value :",dic[i])
            else:
                dic[i] = 1

        for i in dic:
            if dic[i] == 1:
                return i


nums=[2,2,2,2,2,2,1]
obj=Solution().singleNumber(nums=nums)
print(obj)
