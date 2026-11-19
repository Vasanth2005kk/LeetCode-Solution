class Solution:
    def minPartitions(self, n: str) -> int:
        n =  set(n)        
        maxval = 0
        for i in n:
            value = int(i)
            if value >= maxval:
                maxval = value

        return maxval
        

n = "27346209830709182346"
obj = Solution().minPartitions(n)

print(obj)