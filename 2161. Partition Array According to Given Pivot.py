class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        arr1 = []
        arr2 = []

        for i in nums:
            if i <= nums:
                arr1.append(i)
            else:
                arr2.append(i)

        return arr1+arr2