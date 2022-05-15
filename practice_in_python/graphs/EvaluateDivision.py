import collections

class Solution:


    '''
    [["a","b"],["e","f"],["b","e"]]

    [3.4,1.4,2.3]

    [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]

    [["a","e"]]

    [["a","e"],["b","e"]]
    [4.0,3.0]
    [["a","b"],["e","e"],["x","x"]]


    [["a","b"],["c","d"]]
    [1.0,1.0]
    [["a","c"],["b","d"],["b","a"],["d","c"]]
    '''


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(first,prev,al,seen,answers,productSoFar):
            if prev in seen:
                return
            seen.add(prev)
            for neighbor in al[prev]:
                if (first, neighbor) not in answers:
                    answers[(first, neighbor)] = productSoFar * answers[(prev, neighbor)]
                    answers[(neighbor,first)] = 1.0 / (productSoFar * answers[(prev, neighbor)])

                dfs(first,neighbor,al,seen,answers,answers[(first, neighbor)])

        adjLst = collections.defaultdict(list)
        answers = {}
        nodeSet = set()
        # build answer map
        for equation,val in zip(equations, values):
            x,y = equation
            adjLst[x].append(y)
            adjLst[y].append(x)
            nodeSet.update({x,y})
            answers[(x,y)] = val
            answers[(y,x)] = 1.0/val

        for key in nodeSet:
            dfs(key,key,adjLst,set(),answers,1.0)
        # print(answers)
        # print(len(answers))
        # print(nodeSet)

        retVal = []
        # go thru queries
        for x,y in queries:
            if x not in nodeSet or y not in nodeSet:
                retVal.append(-1.0)
            elif x == y:
                retVal.append(1.0)
            elif (x,y) not in answers:
                retVal.append(-1.0)
            else:
                retVal.append(answers[(x,y)])


        return retVal
















