from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        length = len(grid)
        store = []

        for i in range(length):
            store.extend(grid[i])

        for j in store:
            if j < 0:
                count += 1

        return count
    
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
obj = Solution().countNegatives(grid)

print(obj)