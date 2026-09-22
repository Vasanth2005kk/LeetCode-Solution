class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]


letters = ["c","f","j"]
target = "a"
obj = Solution().nextGreatestLetter(letters,target)

print(obj)