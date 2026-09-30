class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letterCount = s.count(letter)
        wordLength = len(s)

        per = int((letterCount /  wordLength) * 100)
        return per


s = "foobar"
letter = "o"

obj = Solution().percentageLetter(s,letter)

print(obj)