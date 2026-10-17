class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic =  {}
        for i in text:
            if i in "balloon":
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] = dic[i] + 1
        

        

text = "nlaebolko"
obj = Solution().maxNumberOfBalloons(text)

print(obj)
