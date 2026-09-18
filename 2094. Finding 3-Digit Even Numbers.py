class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        unique_numbers = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j != k and i != k:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        if num >= 100 and num % 2 == 0:
                            unique_numbers.add(num)
                            
        return sorted(unique_numbers)

digits = [2,1,3,0]

obj = Solution()
result = obj.findEvenNumbers(digits)
print(result)