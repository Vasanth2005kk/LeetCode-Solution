class Solution:
    def maxDepth(self, s: str) -> int: 
        count = 0
        maxValue = 0
        for i in s:
            if i == "(":
                count +=1
                maxValue = max(count,maxValue)
            elif i == ")":
                count -=1

        return maxValue


s = "()(())((()()))"
obj = Solution().maxDepth(s)

print(obj)