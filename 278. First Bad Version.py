# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(bad):
    if bad == 4:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


n = 5

obj = Solution().firstBadVersion(n)
print(obj)