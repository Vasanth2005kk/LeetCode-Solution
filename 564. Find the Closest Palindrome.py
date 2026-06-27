class Solution:
    def nearestPalindromic(self, n: str) -> str: 
        de_count = 0
        de_n=0
            
        n = int(n)
        if len(str(n)) != 1:
            for i in range(n-1,0,-1):
                de_count+=1
                if str(i) == str(i)[::-1] and not(i == n):
                    de_n = i
                    # print("de output :",i)
                    # print("de count :",de_count)
                    break

            in_count = 0
            while True:
                in_count+=1
                n+=1
                if str(n) == str(n)[::-1]:
                    # print("in output :",n)
                    # print("in count :",in_count)
                    break

            if de_count == in_count:
                return str(de_n)
            elif de_count > in_count:
                return str(n)
            else:
                return str(de_n)
        else:
            return str(n-1)

n=45
obj = Solution().nearestPalindromic(n)

print(obj)



class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        length = len(n)
        
        # Handle special cases for single-digit numbers or small numbers
        if num <= 10:
            return str(num - 1)
        if num == 11:
            return "9"
        
        # Generate candidates
        prefix = int(n[:(length + 1) // 2])  # First half of the number
        candidates = set()
        
        # Generate palindromic numbers using the prefix
        for delta in [-1, 0, 1]:  # Adjust the prefix
            new_prefix = str(prefix + delta)
            if length % 2 == 0:  # Even length
                candidate = int(new_prefix + new_prefix[::-1])
            else:  # Odd length
                candidate = int(new_prefix + new_prefix[-2::-1])
            candidates.add(candidate)
        
        # Add edge cases for all 9's and 1 followed by zeros and a 1 (e.g., 999 -> 1001)
        candidates.add(10**length + 1)
        candidates.add(10**(length - 1) - 1)
        
        # Remove the original number itself
        candidates.discard(num)
        
        # Find the closest palindrome
        def compare(x):
            return (abs(x - num), x)  # First sort by distance, then by value
        
        return str(min(candidates, key=compare))
