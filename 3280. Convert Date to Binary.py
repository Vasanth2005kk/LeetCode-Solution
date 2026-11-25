class Solution:
    def convertDateToBinary(self, date: str) -> str:
        Dates = [int(i) for i in date.split("-")]

        ans = []
        for i in Dates:
            BinValue = bin(i).lstrip("0b")
            ans.append(BinValue)

        return "-".join(ans)

date = "2080-02-29"
obj = Solution().convertDateToBinary(date)

print(obj)