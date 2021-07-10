class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l=[1]*n
        r=[1]*n
        c=0
        for i in range(1,n): #left comparison#
            if(ratings[i-1]<ratings[i]):
                l[i]=l[i-1]+1
        for i in range(n-2,-1,-1): #right comparision
            if(ratings[i+1]<ratings[i]):
                r[i]=r[i+1]+1
        for i in range(n): #taking maximum in both
            c+=max(l[i],r[i])
        return c