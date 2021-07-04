#region problem statement

'''

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.


An integer a is closer to x than an integer b if:


|a - x| < |b - x|, or

|a - x| == |b - x| and a < b
 


Example 1:


Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:


Input: arr = [1,2,3,4,5], k = 4, x = -1

Output: [1,2,3,4]
 


Constraints:


1 <= k <= arr.length

1 <= arr.length <= 104

arr is sorted in ascending order.

-104 <= arr[i], x <= 104

'''


#endregion




#region my own unoptimized solution

import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = bisect.bisect_left(arr,x)
        l = []
        if i == 0:
            # store first k elements to the list
            for a in range(k):
                l.append(arr[a])
        elif i == len(arr):
            # store last k elements to the list
            n = len(arr)-1
            for a in range(n,n-k,-1):
                l.append(arr[a])
        else:
            a,b = 0,0
            if arr[i] == x:
                # store x to the list
                l.append(arr[i])
                k-=1
                a,b = i-1, i+1
            # x is not in the list, so check the value at i anyways and check to the left of it
            else:
                a,b = i-1,i
            # store the (k-1)/2 elements from the left and right of x to the list
            while k > 0:
                one = None
                two = None
                if a >= 0:
                    one = arr[a]
                if b < len(arr):
                    two = arr[b]
                if one == None:
                    l.append(two)
                    b+=1
                elif two == None:
                    l.append(one)
                    a-=1
                elif abs(x - two) < abs(x - one) or (abs(x - two) == abs(x - one) and two < one):
                    l.append(two)
                    b+=1
                elif abs(x - one) < abs(x - two) or (abs(x - two) == abs(x - one) and one < two):
                    l.append(one)
                    a-=1
                k-=1
        return sorted(l)

#endregion
        
                