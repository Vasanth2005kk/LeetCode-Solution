class Solution:
    def maxProduct(self, n: int) -> int:
        output = []
        while n != 0:
            maximum_product = n%10
            output.append(maximum_product)
            n = n//10
        output.sort()
        return output[-1] * output[-2]


n = 124

obj = Solution().maxProduct(n)

print(obj)