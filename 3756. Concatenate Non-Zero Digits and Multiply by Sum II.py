from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        output  = []
        for i in queries:
            added = ""
            value = 0
            for j in s[i[0]:i[1]+1:]:
                if j != "0" :
                    added += j
                    value += int(j)
            if added :
                ans = (int(added) * value) % (10**9+7)
                print(ans)
                output.append(ans)
            else:
                output.append(value)
        return output


s = "1000"
queries = [[0,3],[1,1]]


obj = Solution().sumAndMultiply(s,queries)

print(obj)