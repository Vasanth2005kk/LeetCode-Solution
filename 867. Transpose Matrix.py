
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        row = len(matrix)
        column = len(matrix[0])

        # Create independent rows
        trans = [[None] * row for _ in range(column)]

        for i in range(row):
            for j in range(column):
                trans[j][i] = matrix[i][j]

        return trans


matrix = [[1, 2, 3], [4, 5, 6]]

obj = Solution().transpose(matrix)
print(obj)
