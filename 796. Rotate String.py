class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        output = ""
        for i in range(len(s)):
            deleteValue = s.pop()
            s.insert(0,deleteValue)
            output = "".join(s)
            if output == goal:
                return True
            
        return False


s = "abcde"
goal = "cdeab"

obj = Solution().rotateString(s,goal)

print(obj)