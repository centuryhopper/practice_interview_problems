class Solution:
    '''
    [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

    184 + 259 + 577
    + 54 + 118 + 667
    '''

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort by difference
        costs.sort(key=lambda c:c[0]-c[1])
        # print(costs)
        ans = 0
        n = len(costs)//2
        # send the first half to city a, and the rest to city b
        for i in range(n):
            ans += costs[i][0] + costs[i+n][1]
        return ans





