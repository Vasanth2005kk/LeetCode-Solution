from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        Dic =  {}

        duarr = arr.copy()
        duarr = list(set(duarr))
        duarr.sort()
        count = 1

        for i in duarr:
            Dic[i] = count 
            count+=1
        
        output = []
        for j in arr:
            output.append(Dic[j])

        return output


arr = [100,100,100]
obj =  Solution().arrayRankTransform(arr)

print(obj)