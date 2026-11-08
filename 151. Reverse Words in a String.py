class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()[::-1]
        return " ".join(word)

s = "a good   example"

obj = Solution().reverseWords(s)
print(obj)