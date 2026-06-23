class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        total = 0
        for i in str(n):
            total += int(i)

        return total


n = 122

obj = Solution().digitFrequencyScore(n)
print(obj)