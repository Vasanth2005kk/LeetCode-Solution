class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)

        for i in range(0, len(chars), 2 * k):
            chars[i:i + k] = reversed(chars[i:i + k])

        return "".join(chars)



s = "abcdefg"
k = 2

obj = Solution().reverseStr(s,k)
print(obj)