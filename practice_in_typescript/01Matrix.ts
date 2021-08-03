

// use a queue
function updateMatrix(mat: number[][]): number[][]
{
    // populate queue with 0's coordinates
    let m = mat.length, n = mat[0].length
    let q = []
    for (let i = 0;i < m;++i)
    {
        for (let j = 0; j < n; ++j)
        {
            if (mat[i][j] == 1)
                mat[i][j] = -1
            else
                q.push([i,j])
        }
    }
    
    // console.log(mat)
    
    // perform bfs
    let distance = 0
    const dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    while (q.length > 0)
    {
        ++distance
        // get size to visited neighbors
        let size = q.length
        while (size-- > 0)
        {
            let [x,y] = q.shift()
            
            // try to go in all possible directions
            for (const [a,b] of dirs)
            {
                let newX = x+a, newY = y+b
                // make sure coordinates aren't out of bounds and that they aren't other 0s in our matrix
                if (newX < 0 || newY < 0 || newX >= m || newY >= n || mat[newX][newY] != -1)
                    continue
                // add this 1's coordinates into the queue for finding other neighboring 1s
                q.push([newX,newY])
                // update this 1's distance from the original 0 that is being BFSed on
                mat[newX][newY] = distance
            }
        }
    }
    
    return mat
};




                    
                    
            