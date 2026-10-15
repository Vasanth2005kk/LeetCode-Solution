class Solution:
    def numTrees(self, n: int) -> int:
        res = 1

        for i in range(2, n + 1):
            res = (res * (4 * i - 2)) // (i + 1)

        return res


# forumla : cn = 1/n+1 * (2n n) = 1/n+1 * (2n)! / (n! * n!) = (2n)! / (n! * (n+1)!)


obj = Solution()
print(obj.numTrees(3))  # Output: 5