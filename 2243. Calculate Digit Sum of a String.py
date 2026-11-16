class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            length = len(s)
            string = ""
            index = 0
            store = []

            while index < length:
                if len(store) == k:
                    string += str(sum(store))
                    store = []

                store.append(int(s[index]))
                index +=1
            
            if store:
                string += str(sum(store))

            s = string

        return str(s)



s = "11111222223"
k = 3

obj = Solution().digitSum(s,k)
print(obj)