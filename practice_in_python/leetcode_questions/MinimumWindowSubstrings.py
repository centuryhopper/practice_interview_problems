from collections import defaultdict

#region failed attempt
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s), len(t)
        # edge case
        if m < n: return ''
        if t in s: return t
        sett = set(t)
        ttot = 0
        for c in t:
            ttot += ord(c)
        # slide window across s
        i,j = 0,0
        stot = 0
        ret = ''
        while i <= m - n:
            # we need to expand our window either to the end of the string or when we've found a match, whichever one comes first
            while j < m:
                if s[j] in sett:
                    stot += ord(s[j])
                j+=1
            # finally found a match
            if stot >= ttot:
                potential = s[i:j]
                if len(potential) < len(ret) or not ret:
                    ret = potential
                print(ret)
            # no point in continuing sliding window, just return ret
            # if j == m: print(s[i]); break
                
            
            
            # move i to the next character in the window range
            # such that the character is in t
            stot,oldI = 0,i
            for x in range(i+1,j):
                if s[x] in sett:
                    i = x; break
            # edge case (i should change, but if it doesn't, then we handle it here)
            if oldI == i: print('old i is the same as new i');break
            j = i
            # print(s[i])
        return ret
#endregion


#region online solution by https://www.youtube.com/watch?v=T9Mkjh_ZF80
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s), len(t)
        # edge case
        if m < n: return ''
        if t in s: return t
        dt = defaultdict(int)
        for c in t:
            dt[c] += 1
        # slide window across s
        i,j = 0,0
        cnt = n
        minStart = 0
        minLen = 10**9
        while j < m:
            endS = s[j]
            # check end character for validity
            if dt[endS] > 0: cnt-=1
            dt[endS]-=1
            j+=1
            while cnt == 0:
                # update min length
                if minLen > j-i:
                    minLen = j-i
                    minStart = i
                # update what we're about to give up since we're moving the start window pointer
                # forward
                startS = s[i]
                dt[startS]+=1
                if dt[startS] > 0: cnt+=1
                i+=1
        return '' if minLen == 10**9 else s[minStart:minStart+minLen]
#endregion
            
            
            






