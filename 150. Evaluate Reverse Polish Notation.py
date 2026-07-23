from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+","-","*","/"]:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "/":
                    Value = int(a/b)
                elif i == "*":
                    Value = a*b 
                elif i == "-":
                    Value = a-b
                else:
                    Value = a+b
                stack.append(str(Value)) 
                continue

            stack.append(i)
        return int(stack[0])

tokens = ["4","13","5","/","+"]
obj = Solution().evalRPN(tokens)

print(obj)