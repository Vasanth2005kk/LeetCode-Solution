class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]= dic[i]+1
            else:
                dic[i] = 1
    
        new_dic = sorted(dic.items(),reverse=True,key=lambda item : (item[1],item[0]))
        output = ""
        for val in new_dic:
            output += val[0]*val[1]

        return output
s = "tree"
obj = Solution().frequencySort(s)

print(obj)