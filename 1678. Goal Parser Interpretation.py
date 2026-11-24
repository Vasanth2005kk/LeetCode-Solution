class Solution:
    def interpret(self, command: str) -> str:
        output = []

        for i in range(len(command)):
            if command[i] == "G":
                output.append("G")
            elif command[i] == "(":
                if command[i + 1] == ")":
                    output.append("o")
                elif command[i + 1] == "a":
                    output.append("al")

        return "".join(output)



command = "G()(al)"
command = "G()()()()(al)"
command = "(al)G(al)()()G"
obj = Solution().interpret(command)
print(obj)