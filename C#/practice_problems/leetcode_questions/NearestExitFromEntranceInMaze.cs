using System;
using System.Collections.Generic;

public class Solution
{
    /*

    [
        ["+",".","+","+","+","+","+"],
        ["+",".","+",".",".",".","+"],
        ["+",".","+",".","+",".","+"],
        ["+",".","e",".","+",".","+"],
        ["+","+","+","+","+",".","+"]
    ]
        entrance = [3,2]
    */
    public int NearestExit(char[][] maze, int[] entrance)
    {
        // bfs approach
        int m = maze.Length, n = maze[0].Length;
        var q = new Queue<(int,int,int)>();
        q.Enqueue((entrance[0], entrance[1], 0));
        var seen = new HashSet<(int,int)>();

        while (q.Count > 0)
        {
            // get current node
            var (x,y,currentLevel) = q.Dequeue();
            if (seen.Contains((x,y)))
                continue;
            seen.Add((x,y));
            // Console.WriteLine($"{x}, {y}, {z}");

            // if current node is an entrance node,
            // then just return counted steps

            // make sure we're not at the entrance
            if (currentLevel != 0 && (x == 0 || y == 0 || x == m-1 || y == n-1))
                return currentLevel;
            // check neighbors and enqueue valid ones.
            foreach (var neighbor in
                new (int,int)[]
                {
                    (0,1),(0,-1),(-1,0),(1,0)
                }
            )
            {
                var (newX,newY) = neighbor;
                // check bounds
                if (x+newX < 0 || x+newX == m || y+newY < 0 || y+newY == n)
                {
                    continue;
                }
                // avoid walls
                if (maze[x+newX][y+newY] == '+')
                {
                    continue;
                }

                // MUST be an empty cell at this point
                q.Enqueue((x+newX,y+newY,currentLevel+1));
            }
        }

        // cant find a valid path to the exit
        return -1;
    }
}