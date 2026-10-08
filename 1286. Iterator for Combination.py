class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinationValues =  self.combinations(characters,combinationLength)
        print(self.combinationValues)
        self.index = -1
        self.combinationValuesLength = len(self.combinationValues)

    def combinations(self,s, k):
        result = []

        def backtrack(start, current):
            if len(current) == k:
                result.append("".join(current))
                return

            for i in range(start, len(s)):
                current.append(s[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result
    
    def next(self) -> str:
        self.index +=1
        ans = self.combinationValues[self.index]
        return ans

    def hasNext(self) -> bool:
        return self.index < self.combinationValuesLength -1




# Your CombinationIterator object will be instantiated and called as such:
arr = ["abc", 2]
characters= arr[0]
combinationLength = arr[1]

itr = CombinationIterator(characters, combinationLength)

print(itr.next())    # return "ab"
print(itr.hasNext()) # return True
print(itr.next())    # return "ac"
print(itr.hasNext()) # return True
print(itr.next())    # return "bc"
print(itr.hasNext()) # return False