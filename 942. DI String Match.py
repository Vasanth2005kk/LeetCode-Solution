class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        left = 0
        right = len(s)
        perm = []

        for ch in s:
            if ch == 'I':
                perm.append(left)
                left += 1
            else:
                perm.append(right)
                right -= 1

        perm.append(left)

        return perm

s = "IDID"
obj = Solution().diStringMatch(s)

print(obj)