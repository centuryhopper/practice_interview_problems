


/*
Find the connected components of the graph. To find connected components, you can use Union Find (Disjoint Sets), BFS, or DFS.	
For a node u, the number of nodes that are unreachable from u is the number of nodes that are not in the same connected component as u.
The number of unreachable nodes from node u will be the same for the number of nodes that are unreachable from node v if nodes u and v belong to the same connected component.
*/





/*
0 - 2
|   |
5 - 4

3

1 - 6
SIZE = 0

[0,3], [0,1], [0,6] => size = 3
multiply size by number of elements in the group with 0
SIZE = SIZE + size * 4 = 12 in this case since there are 4 elements in that group

repeat procedure for the rest...
[3,1], [3,6] => size = 2
SIZE = SIZE + size * 1 = 14

no more groups to compare for the 1 - 6 component

...so DONE

11
[[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]]
*/

const _ = require('lodash')

function countPairs(n: number, edges: number[][]): number
{
    var parent = [...Array(n).keys()]
    var rank = Array(n).fill(1)
    var find = (x) => {
        if (x === parent[x]) return x
        parent[x] = find(parent[x])
        return parent[x]
    }
    var union = (x,y) => {
        const xr = find(x), yr = find(y)
        if (xr === yr) return
        if (rank[xr] > rank[yr])
            parent[yr] = xr
        else if (rank[yr] > rank[xr])
            parent[xr] = yr
        else
        {
            parent[yr] = xr
            rank[xr] += 1
        }
    }
    var ans : number = 0
    for (const [x,y] of edges)
    {
        union(x,y)
    }

    for (const [x,y] of edges)
    {
        union(x,y)
    }



    // sanity check
    console.table(parent)
    var cnter = _.countBy(parent)
    // console.log(cnter)
    // console.log(typeof(cnter))


    var curSum = _.sum(Object.values(cnter))
    // console.log(curSum)
    // console.log(typeof(curSum))

    for (const [k,v] of Object.entries(cnter))
    {
        // console.log(k,v)
        // console.log(typeof(k),typeof(v))
        var add : number = Number(v) * (curSum - Number(v))
        ans += add
        curSum -= Number(v)
    }




    return ans
};
