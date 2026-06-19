from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = []
        for i  in nums:
            arr.append(int(i))

        arr.sort()
        index = k - k*2
        return str(arr[index])
        

nums = ["3","6","7","10"]
k = 4
obj =  Solution().kthLargestNumber(nums,k)

print(obj)