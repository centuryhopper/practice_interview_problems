import itertools
from heapq import heappush,heapify

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.allCombinations = list(itertools.combinations(characters, combinationLength))
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return "".join(self.allCombinations[self.count-1])

    def hasNext(self) -> bool:
        return self.count < len(self.allCombinations)


class CombinationIterator:


    def __init__(self, chars: str, combinationLength: int):
        # will contain all combinations
        # of chars of the specified length
        # should be no greater than len(chars) choose combinationLength size
        self.lst = []
        heapify(self.lst)
        self.chars = chars
        self.comb = combinationLength
        self.it = 0
        self.rec(self.chars,self.comb,0,'')

        # self.lst should be all populated here
        # print(self.lst)

    def rec(self,chars:str,combLen:int,curPos:int,acc:str)->None:
        # if combLen has been exhausted, add the current string into the heap
        if combLen == 0:
            heappush(self.lst,acc)
            return
        # prevent out of bounds (one possibility of coming here is if our curPos pointer reaches the end of the input string before combLen is exhausted)
        if curPos >= len(chars):
            return
        # take the character at the current position, therefore exhausting combLen
        self.rec(chars,combLen-1,curPos+1,acc + chars[curPos])
        # dont take the character at the current position
        self.rec(chars,combLen,curPos+1,acc)

    def next(self) -> str:
        pass
        ans = self.lst[self.it]
        self.it+=1
        return ans
    def hasNext(self) -> bool:
        return self.it < len(self.lst)

# for val in self.lst:
    # # enforce 26 digits
    #     print(format(val,'026b'))
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# failed attempt
# class CombinationIterator:

#     '''
#     abc = 11100000000000000000000000

#     # all combos for abc
#     [11000000000000000000000000,
#     10100000000000000000000000,
#     01100000000000000000000000]

#     11100000000000000000000000


#     1 & 1 = 1
#     1 & 0 = 0


# ["CombinationIterator","hasNext","next","hasNext","hasNext","next","next","hasNext","hasNext","hasNext","hasNext"]
# [["chp",1],[],[],[],[],[],[],[],[],[],[]]

# ["CombinationIterator","hasNext","next","next","hasNext","next","hasNext","next","hasNext","next","next"]
# [["ahijp",2],[],[],[],[],[],[],[],[],[],[]]

# ["fik","fil","fin","fiu","fiy","fkl","fkn","fku","fky","fln","flu","fly","fnu","fny","fuy","ikl","ikn","iku","iky","iln","ilu","ily","inu","iny","iuy","kln","klu","kly","knu","kny","kuy","lnu","lny","luy","nuy"]

#     '''

#     def __init__(self, chars: str, combinationLength: int):
#         # will contain all combinations
#         # of chars of the specified length
#         self.lst = set()
#         self.chars = chars
#         self.comb = combinationLength
#         self.bitmask = 0
#         self.it = 0
#         # mark all the values where each char is present
#         for c in self.chars:
#             # 26 letters in the alphabet, but bits are 0-indexed
#             self.bitmask = self.flipLetterOn(self.bitmask,c)
#         # print(bin(self.num))
#         self.rec(0,self.comb,self.bitmask)

#         # self.lst should be all populated here
#         self.lst = sorted(self.lst)
#         print(self.lst)

#     def rec(self,i:int,comb:int,bitmask:int)->None:
#         if comb == 0:
#             val = self.toChars(bitmask)
#             self.lst.add(val)
#             return
#         for x in range(i,len(self.chars)-comb+1):
#             bitmask = self.flipLetterOff(bitmask,self.chars[x])
#             self.rec(i+1,comb-1,bitmask)
#             bitmask = self.flipLetterOn(bitmask,self.chars[x])

#     def isLetterOn(self,num:int,c:str)->bool:
#         return num & (1 << 25 - (ord(c)-97))
#     def flipLetterOn(self,num:int,c:str)->int:
#         return num | (1 << 25 - (ord(c)-97))
#     def flipLetterOff(self,num:int,c:str)->int:
#         return num & ~(1 << 25 - (ord(c)-97))
#     def toChars(self,num:int) -> str:
#         ans = ''
#         # a to z
#         for c in self.chars:
#             if self.isLetterOn(num,c):
#                 ans+=c
#         return ans
#     def next(self) -> str:
#         pass
#         # ans = self.lst[self.it]
#         # self.it+=1
#         # return ans
#     def hasNext(self) -> bool:
#         return self.it < len(self.lst)



# # for val in self.lst:
#     # # enforce 26 digits
#     #     print(format(val,'026b'))
# # Your CombinationIterator object will be instantiated and called as such:
# # obj = CombinationIterator(characters, combinationLength)
# # param_1 = obj.next()
# # param_2 = obj.hasNext()