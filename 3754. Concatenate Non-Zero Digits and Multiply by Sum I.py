class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        value = ""
        total = 0
    
        for i in str(n):
            if i == "0":
                continue
            else:
                value +=i
                total += int(i)
        return int(value) * total
                
n = 10203004
obj = Solution().sumAndMultiply(n)

print(obj)

"""
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        allsum = 0
        value = ""
        while n != 0:
            lastValue =  n%10
            remaindValue = n//10
            n =  remaindValue
            if lastValue != 0:
                allsum+=lastValue
                value+=(str(lastValue))

        return int(value[::-1]) * allsum
"""