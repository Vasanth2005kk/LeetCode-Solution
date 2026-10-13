
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        total = 0

        for word in words:
            check = True

            for ch in set(word):
                if word.count(ch) > chars.count(ch):
                    check = False
                    break

            if check:
                total += len(word)

        return total

words = ["cat","bt","hat","tree"]
chars = "atach"

obj = Solution().countCharacters(words,chars)
print(obj)