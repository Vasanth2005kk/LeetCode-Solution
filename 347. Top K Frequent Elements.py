from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i]=1
        # print(dic)

        new_dic = sorted(dic.items(),reverse=True,key =lambda item : (item[1], item[0]))
        output = []
        # print(new_dic)
        for i in new_dic:
            output.append(i[0])
            if len(output) == k:
                output.sort()
                return output

nums = [1]
k = 1

obj = Solution().topKFrequent(nums,k)
print(obj)