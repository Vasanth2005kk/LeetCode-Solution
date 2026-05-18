from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for value in s:
            stack.append(value)

        for index in range(len(stack)):
            s[index] = stack.pop()
    
        return s

s=["h","e","l","l","o"]

obj = Solution().reverseString(s)

print(obj)