class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        output = []
        for i in matrix:
            output.append(sum(i))
        
        return output
    

matrix = [[0,1,1],[1,0,1],[1,1,0]]

obj = Solution().findDegrees(matrix=matrix)
print(obj)