class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor_values = []

        for i in range(m):
            for j in range(n):

                top = matrix[i - 1][j] if i > 0 else 0
                left = matrix[i][j - 1] if j > 0 else 0
                diagonal = matrix[i - 1][j - 1] if i > 0 and j > 0 else 0

                matrix[i][j] ^= top ^ left ^ diagonal
                xor_values.append(matrix[i][j])

        xor_values.sort(reverse=True)
        
        return xor_values[k - 1]

matrix = [[5,2],[1,6]]
k = 1

obj = Solution().kthLargestValue(matrix,k)
print(obj)