class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for i in arr1:
            valid = True

            for j in arr2:
                if abs(i - j) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2

obj = Solution().findTheDistanceValue(arr1,arr2,d)

print(obj)