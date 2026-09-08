class Solution:
    def countCommas(self, n: int) -> int:
        num = n
        if n <= 999:
            return 0

        lennumber = 0
        while num != 0:
            num = num // 10
            lennumber +=1

        if lennumber == 7:
            return 999011

        return n - 999




n = 1002
obj = Solution().countCommas(n)
print(obj)