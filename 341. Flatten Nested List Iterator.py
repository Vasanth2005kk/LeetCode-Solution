# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       pass

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       pass

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       pass

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]) -> None:
        self.stack = []
        self.dfs(nestedList)

    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, nestedList: [NestedInteger]) -> None:
        for nested in reversed(nestedList):
            if nested.isInteger():
                self.stack.append(nested.getInteger())
            else:
                self.dfs(nested.getList())


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# [
#     NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, 
#     NestedInteger{_integer: 1, _list: []}]}, 
#     NestedInteger{_integer: 2, _list: []}, 
#     NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, 
#     NestedInteger{_integer: 1, _list: []}]}
# ]

# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]


# NestedInteger{_integer: None, _list: [NestedInteger{_integer: 1, _list: []}, NestedInteger{_integer: 1, _list: []}]}