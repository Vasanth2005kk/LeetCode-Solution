class Solution:
    def minRotations(self, s: str) -> int:
        From = 0
        total = 0

        for i in s:
            To = int(i)
            distance = abs(From - int(To))
            CirDistance = 10 - distance

            Value = min(distance,CirDistance)
            total += Value
            From = To

        return total

s = "0192837465"
s = "1200210200"

obj = Solution().minRotations(s)
print(obj)