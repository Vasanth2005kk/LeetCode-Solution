class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        output = []
        stack = []

        for i in range(1,n+1):
            if stack == target:
                return output
            if i in target:
                stack.append(i)
                output.append("Push")
            else:
                output.extend(["Push","Pop"])

        return output


target = [1,2]
n = 4

obj = Solution().buildArray(target,n)
print(obj)

