class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        output = []

        n = len(nums)

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c = b + 1
                d = n - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    if total == target:
                        output.append([
                            nums[a],
                            nums[b],
                            nums[c],
                            nums[d]
                        ])

                        c += 1
                        d -= 1

                        while c < d and nums[c] == nums[c - 1]:
                            c += 1

                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1

                    elif total < target:
                        c += 1

                    else:
                        d -= 1

        return output

nums = [1,0,-1,0,-2,2]
target = 0

obj = Solution().fourSum(nums,target)

print(obj)