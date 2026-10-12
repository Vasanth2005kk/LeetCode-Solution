
class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = [0]
        length = 0

        # Step 1: Calculate the length after each operation
        for ch in s:
            if ch == "#":
                length *= 2
            elif ch == "*":
                length = max(0, length - 1)
            elif ch == "%":
                pass
            else:
                length += 1

            lengths.append(length)

        if k >= length:
            return "."

        # Step 2: Trace the required index backward
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev_length = lengths[i]
            curr_length = lengths[i + 1]

            if ch == "#":
                if prev_length > 0:
                    k %= prev_length

            elif ch == "*":
                pass

            elif ch == "%":
                k = curr_length - 1 - k

            else:
                if k == prev_length:
                    return ch

        return "."




s="%#bz%xum##i##vzo#pwc*#dkwbh####%uf%s*%cgppqhqa%h#l##o%ij%%cz%iga##e###u%#e####jfwx##%%*x%m*%#"
k = 6523
obj = Solution().processStr(s,k)
print(obj)