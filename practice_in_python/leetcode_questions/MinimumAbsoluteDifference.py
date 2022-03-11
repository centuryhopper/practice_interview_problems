class Solution:
    '''
    [-14, -10, -4, 3, 8, 19, 23, 27]
    
    '''
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diffLookup = collections.defaultdict(list)
        for i in range(1,len(arr)):
            diffLookup[arr[i] - arr[i-1]].append((arr[i-1],arr[i]))
        return diffLookup[min(diffLookup.keys())]
        
        