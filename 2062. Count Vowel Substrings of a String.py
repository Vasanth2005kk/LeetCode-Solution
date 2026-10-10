
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"
        length = len(word)
        count = 0

        for left in range(length):
            seen = set()

            for right in range(left, length):
                if word[right] not in vowels:
                    break

                seen.add(word[right])

                if len(seen) == 5:
                    count += 1

        return count


word ="aeiouu"
obj = Solution().countVowelSubstrings(word)
print(obj)
