class Solution:
    '''

    [5,1,2,3,4]
    [4,4,1,5,1]

    5-4 + 1-4 + 2-1 + 3-5 + 4-1 = 1-3+1-2+3 = 0 cant have negative profit anywhere, so this doesn't work

    4-1 + 5-4 + 1-4 + 2-1 + 3-5 = 3+1-3+1-2 = 0 This one works because at no point in time do we have negative profit when traveling

    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        n = len(gas)
        for i in range(n):
            total += gas[i]-cost[i]
        # net total cannot be negative
        if total < 0: return -1
        diff = 0
        start = 0
        for i in range(n):
            diff += gas[i]-cost[i]
            if diff < 0:
                # start at the next station
                start = i+1
                diff = 0


        return start