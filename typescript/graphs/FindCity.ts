// 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance


/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} distanceThreshold
 * @return {number}
 */
var findTheCity = (n, edges, distanceThreshold) =>
{
    // build 2d array
    let dp = Array(n).fill().map(() => new Array(n).fill(Number.POSITIVE_INFINITY))
    // console.log(dp)
    // initialize all values to infinity
    // initialize all nodes' distance to 0
    for (let i = 0; i < n;++i)
    {
        dp[i][i] = 0
    }
    for (const [x,y,z] of edges)
    {
        dp[x][y] = z
        dp[y][x] = z
    }
    // console.log(dp)

    // implement floyd-warshall algorithm
    for (let k = 0; k < n;++k)
    {
        for (let i = 0; i < n;++i)
        {
            for (let j = 0; j < n;++j)
            {
                if (dp[i][j] > dp[i][k] + dp[k][j])
                {
                    dp[i][j] = dp[i][k] + dp[k][j]
                }
            }
        }
    }

    // console.log(dp)


    // count all nodes distances less than or equal to threshold.
    // return the answer with the smallest count
    let [node,cnt] = [Number.POSITIVE_INFINITY,Number.POSITIVE_INFINITY]

    for (let i = 0;i < n;++i)
    {
        let curCnt = 0
        for (let j = 0;j < n;++j)
        {
            curCnt = (dp[i][j] <= distanceThreshold) ? curCnt + 1 : curCnt
        }
	
	// update node and counter if we find a node with a smaller number of reachable nodes within the threshold distance
        if (curCnt < cnt)
        {
            node = i
            cnt = curCnt
        }
	// if we encounter a counter that is matching our current recorded counter, then update our node answer
        else if (cnt == curCnt)
        {
	    // we don't need to check if i > node because the numbers grow with the loop
            node = i
        }
    }

    return node


};

// console.log(n) // undefined

var n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
console.log(findTheCity(n,edges,distanceThreshold))

var n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
console.log(findTheCity(n,edges,distanceThreshold))




