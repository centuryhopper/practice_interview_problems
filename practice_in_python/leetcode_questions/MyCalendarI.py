import bisect

# brute force (TLE)
# class MyCalendar:
#     def __init__(self):
#         self.s = set()
#     def book(self, start: int, end: int) -> bool:
#         st = set(range(start,end))
#         if st & self.s:
#             return False
#         self.s.update(st)
#         return True

# my final solution
# class MyCalendar:
#     def __init__(self):
#         # as problem states, this list will
#         # be at most of size 1000
#         self.lst = []
#     # time: O(n log n + O(n)) => O(n log n)
#     def book(self, start: int, end: int) -> bool:
#         # must pass the four cases of intersection
#         # before adding to the list
#         for s,e in self.lst:
#             # first two covers cases I,II, and III
#             if s <= start <= e:
#                 return False
#             if s <= end-1 <= e:
#                 return False
#             # covers case IV
#             if start < s and end-1 > e:
#                 return False


#         self.lst.append((start,end-1))
#         self.lst.sort()
#         return True



# optimized with binary search (online solution, not my own)
class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False
        i = bisect.bisect_right(self.intervals, start)
        print(f'i: {i}')
        if i % 2:            # start is in some stored interval
            return False
        j = bisect.bisect_left(self.intervals, end)
        print(f'j: {j}')
        # if they're the same, then that means start and end weren't found
        # in the list, so we're definitely good to go
        if i != j:
            return False
        # inserts start and end right before index i
        self.intervals[i:i] = [start, end]
        return True

if __name__ == '__main__':
    l = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
    m = MyCalendar()
    for i,lst in enumerate(l):
        m.book(lst[0], lst[1])
    print(m.intervals)

