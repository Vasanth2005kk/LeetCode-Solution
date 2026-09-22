class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        evenindex = (n + 1) // 2
        oddindex = n // 2

        even_choices = pow(5, evenindex, MOD)
        odd_choices = pow(4, oddindex, MOD)
        
        return (even_choices * odd_choices) % MOD

n = 1
obj = Solution().countGoodNumbers(n)
print(obj)