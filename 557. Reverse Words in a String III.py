class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        output = ""
        for i in s:
            revers = i[::-1]
            output += revers + " "


        return output.strip()


s = "Let's take LeetCode contest"
obj  = Solution().reverseWords(s)
print(obj)