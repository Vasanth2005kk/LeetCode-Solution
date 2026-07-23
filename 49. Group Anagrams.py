from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for index,val in enumerate(strs):
            value = "".join(sorted(val))
            if value in dic:
                dic[value] = dic[value] + [strs[index]]
            else:
                dic[value] = [strs[index]]
        
        return list(dic.values())

strs = ["eat","tea","tan","ate","nat","bat"]

obj = Solution().groupAnagrams(strs)

print(obj)