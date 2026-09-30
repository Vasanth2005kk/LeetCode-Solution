class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

        length = max(len(v1), len(v2))

        for i in range(length):
            num1 = v1[i] if i < len(v1) else 0
            num2 = v2[i] if i < len(v2) else 0

            if num1 < num2:
                return -1

            if num1 > num2:
                return 1

        return 0

version1 = "1.2"
version2 = "1.10"

obj = Solution().compareVersion(version1,version2)

print(obj)