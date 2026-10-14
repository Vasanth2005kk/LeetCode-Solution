class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            total = 1
            for num in str(n):
                total *= int(num)

            if total % t == 0:
                return n

            n+=1



n = 15
t = 3

obj = Solution().smallestNumber(n,t)
print(obj)