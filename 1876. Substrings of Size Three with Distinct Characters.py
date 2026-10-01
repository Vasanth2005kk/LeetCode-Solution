class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        right = 3
        length = len(s)+1

        count = 0
        while left <= length and right != length:
            if len(set(s[left:right])) == 3:
                count +=1
            left+= 1
            right += 1

        # print(count)
        return count

s = "xyzzaz"
# s = "aababcabc"

obj = Solution()
print(obj.countGoodSubstrings(s))