
myAns = [True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False]
correctAns = [True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False]
queries = [[9,7],[7,3],[6,1],[1,8],[5,7],[3,8],[2,5],[7,9],[3,0],[4,8],[5,1],[5,3],[3,0],[9,8],[6,9],[5,0],[8,2],[3,6],[3,6],[1,0],[9,7],[9,5],[1,9],[0,4],[7,3],[9,8],[6,2],[7,9],[8,9],[0,5],[5,8],[9,8],[5,6],[7,6],[7,3],[2,1],[9,8],[8,2],[7,8],[9,8],[0,1],[8,9],[8,9],[6,1],[8,1],[8,6],[3,8],[8,9],[9,7],[8,7],[3,7],[9,7],[9,6],[4,2],[5,9],[3,0],[6,9],[7,8],[6,9],[2,1],[7,3],[0,5],[4,9],[5,6],[8,7],[9,7],[9,3],[1,0],[1,7],[7,9],[1,5]]
i = 0
for x,y in zip(myAns,correctAns):
    if x != y:
        print(queries[i])
    i+=1


