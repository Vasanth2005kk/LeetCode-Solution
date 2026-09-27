class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        for key , value in knowledge:
            if key in s:
                s = s.replace(f"({key})",value)
        
        Checking = ""
        stack = []
        for chr in s:
            if chr == "(":
                stack.append("(")
            elif chr == ')':
                s = s.replace(f"({Checking})","?")
                Checking  = ""
                stack.pop()
            elif stack:
                Checking += chr
            
        return s



s = "hi(name)"
knowledge = [["a","b"]]

obj = Solution().evaluate(s,knowledge)
print(obj)