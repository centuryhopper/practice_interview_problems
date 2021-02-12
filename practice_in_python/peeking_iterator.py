# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
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
        self.tmp = self.iterator.next() if self.iterator.hasNext() else None

    # get the value at where the current pointer is (no pointer movement done)
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.tmp

    # get the current value, move the pointer to the next one and return the current value

    def next(self):
        """
        :rtype: int
        """
        retVal = self.tmp
        self.tmp = self.iterator.next() if self.iterator.hasNext() else None
        return retVal

    # return whether or not the current point is less than the index of the last element (length - 1)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.tmp is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
