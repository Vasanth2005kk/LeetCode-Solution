class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        row = len(mat)
        lastindex = -1
        total = 0
        mid = 0 
        if row % 2 == 1:
            mid =  row // 2 + 1
        count = 1
        for i in range(row):
            total += mat[i][i]
            if mid == count:
                total -= mat[i][i]            
            total += mat[i][lastindex]
            lastindex -=1
            count +=1

        return total

mat = [[1,2,3],[4,5,6],[7,8,9]]

mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

obj = Solution().diagonalSum(mat)
print(obj)