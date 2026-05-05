class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(' ')
        if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):
            return False
        
        dic =  {}
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != s[i]:
                    return False
            dic[pattern[i]] = s[i]

        return True
    


pattern = "abba"
s = "dog cat cat dog"

obj = Solution().wordPattern(pattern,s)
print(obj)