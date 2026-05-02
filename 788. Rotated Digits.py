class Solution:
    def rotatedDigits(self, n: int) -> int:
        dic ={"0":0,"1":1,"2":5,"5":2,"6":9,"8":8,"9":6}
        count = 0
        added = ''

        for i in range(1,n+1):
            i = str(i)
            if i in ["3","4","7"]:
                continue
            elif  len(i) == 1:
                if dic[i] != int(i):
                    # print("value :",dic[i])
                    count +=1 
            else:
                for single in i:
                    if "3" in i or "4" in i or "7" in i:
                        break 
                    added +=  str(dic[single])
                if added != i and len(added) == len(i):  
                    # print(f"added Value :{added} > type :{type(added)}, i Value {i} > type : {type(i)}")
                    count +=1
                added = ''
        return count


n = 857
obj = Solution().rotatedDigits(n)
print(obj)