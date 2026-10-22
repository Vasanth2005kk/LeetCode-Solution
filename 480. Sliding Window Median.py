
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small = []  # Max heap (negative values)
        large = []  # Min heap
        delayed = defaultdict(int)

        small_size = 0
        large_size = 0
        result = []

        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]

                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal small_size, large_size

            if small_size > large_size + 1:
                prune(small)
                num = -heapq.heappop(small)
                heapq.heappush(large, num)
                small_size -= 1
                large_size += 1
                prune(small)

            elif small_size < large_size:
                prune(large)
                num = heapq.heappop(large)
                heapq.heappush(small, -num)
                large_size -= 1
                small_size += 1
                prune(large)

        def get_median():
            prune(small)
            prune(large)

            if k % 2:
                return float(-small[0])

            return (-small[0] + large[0]) / 2.0

        for i, num in enumerate(nums):
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1

            balance()

            if i >= k:
                outgoing = nums[i - k]
                delayed[outgoing] += 1

                if outgoing <= -small[0]:
                    small_size -= 1
                    if outgoing == -small[0]:
                        prune(small)
                else:
                    large_size -= 1
                    if large and outgoing == large[0]:
                        prune(large)

                balance()

            if i >= k - 1:
                result.append(get_median())

        return result




nums = [5,2,2,7,3,7,9,0,2,3]
k = 9

obj = Solution().medianSlidingWindow(nums, k)

print(obj)



'''
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:

        if k == 1:
            return [float(i) for i in nums]

        start = 0
        end = k
        length = len(nums)

        if k % 2 == 0:
            val = k // 2
            index = (val-1,val)
        else:
            index = k // 2
        output = []
        while end <= length:
            Value = nums[start:end]
            sort_val = sorted(Value)
            if k % 2 == 0:
                ans = float(sort_val[index[0]] + sort_val[index[1]])/2
                output.append(ans)
            else:
                output.append(float(sort_val[index]))

            start+=1
            end += 1

        return output
'''