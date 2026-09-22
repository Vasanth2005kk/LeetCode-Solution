# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            value = (low + high) // 2
            gus = guess(value)
            if gus == 0:
                return value

            elif gus == 1:
                low = value + 1

            else:
                high = value - 1

n = 10
pick = 6

solution = Solution()
result = solution.guessNumber(n)
print(result)
