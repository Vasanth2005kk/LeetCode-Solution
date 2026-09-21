# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator

        # Store the next value
        if self.iterator.hasNext():
            self.value = self.iterator.next()
        else:
            self.value = None

    def peek(self):
        """
        Returns the next element without advancing the iterator.
        :rtype: int
        """
        print("peek :", self.value)
        return self.value

    def next(self):
        """
        :rtype: int
        """
        current = self.value

        # Move to the next value
        if self.iterator.hasNext():
            self.value = self.iterator.next()
        else:
            self.value = None

        print("next :", current)
        return current

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.value is not None


        
# Input
# ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 2, 2, 3, false]
