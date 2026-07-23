class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t= sorted(t)
        if s == t:
            return True
        return False

s="a"
t="ab"

obj = Solution().isAnagram(s,t)
print(obj)



'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t=list(t)

        for i in s:
            if i in t:
                t.pop(t.index(i))
            else:
                return False

        if len(t) != 0:
            return False
        else:
            return True
'''