class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = []
        output = []
        front = 0

        for i in range(len(nums)):
            # Remove indices outside the window
            while front < len(dq) and dq[front] <= i - k:
                front += 1

            # Remove smaller values from the back
            while len(dq) > front and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Store the maximum for each complete window
            if i >= k - 1:
                output.append(nums[dq[front]])

            # Remove consumed elements to keep the list small
            if front > 1000:
                dq = dq[front:]
                front = 0

        return output

"""class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        windows = []

        start = 0
        end = k
        length  = len(nums)

        while end <= length:
            windows.append(set(nums[start:end]))
            start +=1
            end +=1

        output = []
        for i in windows:
            output.append(max(i))

        return output"""

nums = [1,3,-1,-3,5,3,6,7]
k = 3

obj = Solution().maxSlidingWindow(nums,k)

print(obj)