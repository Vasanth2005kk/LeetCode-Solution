class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:

            matrix = [[None]*n]*n
            result = []

            top = 0
            bottom = len(matrix) - 1
            left = 0
            right = len(matrix[0]) - 1

            value = 0
            while top <= bottom and left <= right:

                # Left -> Right
                for i in range(left, right + 1):
                    value +=1
                    matrix[top][i] = value 
                top += 1
                
                # Top -> Bottom
                for i in range(top, bottom + 1):
                    value += 1
                    matrix[i][right] = value
                right -= 1

                # Right -> Left
                if top <= bottom:
                    for i in range(right, left - 1, -1):
                        value +=1
                        matrix[bottom][i] = value
                    bottom -= 1

                # Bottom -> Top
                if left <= right:
                    for i in range(bottom, top - 1, -1):
                        value +=1
                        matrix[i][left] = value
                    left += 1

            return matrix

n = 3
obj  = Solution().generateMatrix(n)
print(obj)