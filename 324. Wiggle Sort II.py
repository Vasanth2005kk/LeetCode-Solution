from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)

        n = len(nums)

        mid = (n - 1) // 2

        end = n - 1

        for i in range(n):
            if i % 2 == 0:
                nums[i] = sorted_nums[mid]
                mid -= 1
            else:
                nums[i] = sorted_nums[end]
                end -= 1

        return nums

obj = Solution()
print(obj.wiggleSort([1, 5, 1, 1, 6, 4]))  # Output: [1, 6, 1, 5, 1, 4]
print(obj.wiggleSort([1, 3, 2, 2, 3, 1]))  # Output: [2, 3, 1, 3, 1, 2]