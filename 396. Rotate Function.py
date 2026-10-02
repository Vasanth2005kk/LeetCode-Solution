class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0

        total_sum = sum(nums)

        # Calculate F(0)
        current = 0
        for i in range(n):
            current += i * nums[i]

        max_value = current

        # Calculate F(1), F(2), ...
        for k in range(1, n):
            current = current + total_sum - n * nums[n - k]

            max_value = max(max_value, current)

        return max_value

nums = [4, 3, 2, 6]

obj = Solution()
print(obj.maxRotateFunction(nums))