class Solution:
    def isBalanced(self, num: str) -> bool:
        oddin = 0
        evenin =0

        for i in range(len(num)):
            if i%2 == 0:
                evenin += int(num[i])
            else:
                oddin += int(num[i])

        if oddin == evenin:
            return True
        return False

num = "1234"
obj = Solution().isBalanced(num)

print(obj)