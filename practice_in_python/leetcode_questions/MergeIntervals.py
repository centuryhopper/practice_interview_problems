class Solution:

    '''
    [[1,4],[4,6],[5,8]]

    [[1,4],[2,3]]

    [[1,4],[2,4]]


    '''

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        # print(intervals)
        def getAnswer(intervals):
            ans = [intervals[0]]
            n = len(intervals)

            for i in range(1,n):
                curStart,curEnd = intervals[i]
                prevStart,prevEnd = ans[-1]
                if curStart <= prevEnd and prevEnd <= curEnd:
                    ans[-1][1] = curEnd
                elif curEnd > prevEnd:
                    ans.append(intervals[i])

            return ans

        ans = getAnswer(intervals)

        return ans





