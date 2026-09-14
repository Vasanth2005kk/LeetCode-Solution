from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        if rec1[0] < rec2[2] and rec1[2] > rec2[0] and rec1[1] < rec2[3] and rec1[3] > rec2[1]:

            return True

        return False


rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

obj = Solution().isRectangleOverlap(rec1,rec2)
print(obj)