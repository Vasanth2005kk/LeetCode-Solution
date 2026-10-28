class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip("aeiou")


s = "idea"

obj = Solution().trimTrailingVowels(s)
print(obj)