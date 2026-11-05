class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        output = s[:k:][::-1] + s[k::]
        return output

s = "abcd"
k = 2

obj = Solution().reversePrefix(s,k)
print(obj)