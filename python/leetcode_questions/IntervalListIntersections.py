class Solution:
    '''
    [[0,2],[5,10],[13,23],[24,25]]
    [[1,5],[8,12],[15,24],[25,26]]
    '''
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        if not fl or not sl: return []
        n1,n2 = len(fl),len(sl)
        i=j=0
        ans = []
        while i < n1 and j < n2:
            si,ei=fl[i]
            sj,ej=sl[j]
            #region not intersecting
            if si < sj and ei < sj:
                i+=1
            elif sj < si and ej < si:
                j+=1
            #endregion
            #region complete intersections
            elif si >= sj and ei<=ej:
                ans.append(fl[i])
                i+=1
            elif sj >= si and ej<=ei:
                ans.append(sl[j])
                j+=1
            #endregion

            #region partial intersections
            elif ei < ej and ei >= sj:
                ans.append([sj,ei])
                i+=1
            elif ej < ei and ej >= si:
                ans.append([si,ej])
                j+=1
            #endregion

        return ans

