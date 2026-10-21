class Solution:
    def trimMean(self, arr: list[int]) -> float:
        length = len(arr)
        removeElement = int(length*(5/100))
        print(f"Length of Array {length} to remove element : {removeElement}")
        arr.sort()
        total = 0
        for i in range(removeElement,length-removeElement):
            total += arr[i]

        return  float(f"{total / (length-(removeElement+removeElement)):.5f}")


arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
obj = Solution().trimMean(arr)

print(obj)