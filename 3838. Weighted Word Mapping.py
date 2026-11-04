from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        output = ""
        letters = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
        total = 0
        for i in words:
            for j in i:
                total += weights[ord(j) - 97]
            index =  (total % 26)
            output += letters[index]
            total = 0

        return output

words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

obj = Solution().mapWordWeights(words,weights)
print(obj)