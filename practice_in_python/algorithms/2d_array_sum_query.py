


def sumQuery(lst:list[list[int]]) -> list[list[int]]:

    m, n = len(lst)+1, len(lst[0])+1
    queryLst = [[0]*(n) for _ in range(m)]

    # fill second column (offsetting the lst index by - 1)
    for i in range(1, n):
        # current sum is the sum of the current value in
        # lst plus the total sum of the value directly above
        queryLst[i][1] = lst[i-1][0] + queryLst[i-1][1]
    # fill second row (offsetting the lst index by - 1)
    for i in range(1, m):
        # current sum is the sum of the current value in
        # lst plus the total sum of the value directly to the left
        queryLst[1][i] = lst[0][i-1] + queryLst[1][i-1]
        # print(lst[0][i-1], queryLst[0][i-1])
    # print()

    for i in range(2,m):
        for j in range(2,n):
            queryLst[i][j] = queryLst[i-1][j] + queryLst[i][j-1] + lst[i-1][j-1] - queryLst[i-1][j-1]
    for l in queryLst:
        print(l)

    return

# def sumRows(lst:list[list[int]]) -> list[list[int]]:



if __name__ == '__main__':

    lst = \
    [
        [2,0,-3,],
        [6,3,2,],
        [5,4,7,],
        [2,-6,8,],
    ]

    m,n = len(lst), len(lst[0])

    # column major printing
    for i in range(n):
        for j in range(m):
            print(lst[j][i], end=' ')
        print()

    # row major printing
    # for i in range(m):
    #     for j in range(n):
    #         print(lst[i][j], end=' ')
    #     print()


    # sumQuery([
    #     [0,1,0],
    #     [1,1,1],
    #     [0,1,0]])










