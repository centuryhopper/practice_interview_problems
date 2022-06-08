
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalPoints = sum(cardPoints)
        if len(cardPoints) == k: return totalPoints

        retVal = 0
        n = len(cardPoints)
        # window of elimination
        window = n - k

        # get first n-k elements
        sumOfCurrentWindow = sum(cardPoints[:n-k])

        for i in range(k+1):
            # uppper and lower bound of current window of points to not add
            lb = i
            ub = i + window
            # print(lb, ub)
            if ub > n: break
            if lb > 0:
                # drop the previous head element
                sumOfCurrentWindow -= cardPoints[lb-1]
                # add the next tail element
                sumOfCurrentWindow += cardPoints[ub-1]

            retVal = max(retVal, totalPoints - sumOfCurrentWindow)
            # print(lb,ub,retVal)
        return retVal




# more optimized solution
# class Solution:
#     # https://www.youtube.com/watch?v=U0utLw_vWGM
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         totalPoints = sum(cardPoints)
#         if len(cardPoints) == k: return totalPoints

#         retVal = 0
#         n = len(cardPoints)
#         # window of elimination
#         window = n - k

#         # get first n-k-1 elements
#         sumOfCurrentWindow = sum(cardPoints[:window-1])

#         for i in range(window-1, n):
#             # add tail card
#             sumOfCurrentWindow += cardPoints[i]

#             retVal = max(retVal, totalPoints - sumOfCurrentWindow)

#             # drop head card
#             sumOfCurrentWindow -= cardPoints[i - (window-1)]
#         return retVal













# Failed attempts

# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         totalPoints = sum(cardPoints)
#         if len(cardPoints) == k: return totalPoints

#         retVal = 0
#         n = len(cardPoints)
#         # window of elimination
#         window = n - k

#         for i in range(k+1):
#             # uppper and lower bound of current window of points to not add
#             lb = i
#             ub = i + window
#             # print(lb, ub)
#             if ub > n: break
#             sumOfCurrentWindow = sum(cardPoints[i:ub])
#             retVal = max(retVal, totalPoints - sumOfCurrentWindow)
#             # print(lb,ub,retVal)
#         return retVal














# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:

#         totalPoints = sum(cardPoints)
#         if len(cardPoints) == k: return totalPoints

#         tot = 0
#         n = len(cardPoints)
#         # window of elimination
#         window = n - k

#         for i in range(k+1):
#             # uppper and lower bound of current window of points to not add
#             lb = i
#             ub = i + (window - 1)
#             sumOfCurrentWindow = 0

#             a,b = 0, n - 1
#             while a<lb or b>ub:
#                 if a<lb:
#                     sumOfCurrentWindow += cardPoints[a]
#                     a+=1
#                 if b>ub:
#                     sumOfCurrentWindow += cardPoints[b]
#                     b-=1
#             tot = max(tot, sumOfCurrentWindow)
#         # print(tot)
#         return tot




