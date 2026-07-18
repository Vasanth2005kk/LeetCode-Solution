class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 2 :
            return 1
        setValue =  "122"
        for i in range(3,n+1):
            if len(setValue) >= n:
                ans = setValue[0:n:].count("1")
                return ans
            elif i%2 == 0:
                setValue += ("2" * int(setValue[i-1])) 
            else:
                setValue += ("1" * int(setValue[i-1])) 
n = 6
obj = Solution().magicalString(n)
print(obj)