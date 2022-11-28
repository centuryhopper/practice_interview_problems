from typing import List
import collections

class Solution:
    '''
    winners<int>: {}
    losers<int,int>: {}

    '''
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = collections.defaultdict(int)
        for winner, loser in matches:
            if winner not in losers:
                winners.add(winner)
            winners.discard(loser)
            losers[loser]+=1
        return [sorted(winners), sorted(k for k,v in losers.items() if v == 1)]
