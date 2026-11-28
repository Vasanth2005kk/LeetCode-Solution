
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):

            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child



g = [10,9,8,7]
s = [5,6,7,8]

obj = Solution().findContentChildren(g,s)
print(obj)