



from collections import defaultdict

class Solution:
    '''
    Time: O(N^2), where N^2 is the number of bricks
    Space: O(W), where W is the width of the wall (max number of sums out of all the rows)
    '''
    def leastBricks(self, walls: List[List[int]]) -> int:

        d = defaultdict(int)
        maxEdges = 0
        for wall in walls:
            curSum = 0
            for i in range(len(wall)-1):
                curSum += wall[i]
                d[curSum] += 1
                # a lot of comparisons which isn't as performant
                maxEdges = max(maxEdges, d[curSum])
        # for k,v in d.items():
        #     print(k,v)

        return len(walls) - maxEdges



'''
More optimized solution


from collections import defaultdict

class Solution:
    def leastBricks(self, walls: List[List[int]]) -> int:
        d = defaultdict(int)
        for wall in walls:
            curSum = 0
            # up to but not including the last last brick
            for brick in wall[:-1]:
                curSum += brick
                d[curSum] += 1
        # for k,v in d.items():
        #     print(k,v)
        return len(walls) - max(d.values(), default=0)
'''
