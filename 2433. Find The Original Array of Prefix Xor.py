class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        arr = [pref[0]]

        for i in range(1, len(pref)):
            arr.append(pref[i - 1] ^ pref[i])

        return arr

pref = [5,2,0,3,1]
obj = Solution().findArray(pref)
print(obj)