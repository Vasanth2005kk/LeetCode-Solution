from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        if numRows == 1:
            print(numRows)

        for i in range(numRows-1):
            temp = [0]+output[-1]+[0]
            tem_res = []
            for j in range(len(temp)-1):
                tem_res.append(temp[j]+temp[j+1])
            output.append(tem_res)

        return output
    
numRows =  5

obj  = Solution().generate(numRows)

print(obj)