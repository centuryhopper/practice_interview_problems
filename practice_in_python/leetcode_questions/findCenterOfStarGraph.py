from itertools import chain
from collections import Counter


#region one-liner
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return Counter(chain(*edges)).most_common(1)[0][0]
#endregion