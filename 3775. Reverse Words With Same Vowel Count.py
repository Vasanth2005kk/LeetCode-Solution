class Solution:
    def reverseWords(self, s: str) -> str:
        splitedWord = s.split()
        count = self.VowelCount(splitedWord[0])        
        reverse = splitedWord[0] + " "
        for i in range(1,len(splitedWord)):
            if self.VowelCount(splitedWord[i]) == count:
                reverse += splitedWord[i][::-1] + " "
            else:
                reverse += splitedWord[i] + " "
        return reverse.strip()
    
    def VowelCount(self,word):
        vowelCount = 0
        for i in word:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                vowelCount +=1
        return vowelCount

s = "cat and mice"
s = "book is nice"

obj = Solution().reverseWords(s)
print(obj)