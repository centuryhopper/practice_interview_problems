
using System;

public class SurroundedRegions
{
    private void p(object m) => Console.WriteLine(m);

    private bool IsOutOfBounds(int row, int col, int numRows, int numColumns)
    {
        return (row < 0 || row >= numRows) || (col < 0 || col >= numColumns);
    }

    private void DepthFirstSearch(char[][] a, int r, int c)
    {
        if (IsOutOfBounds(r, c, a.Length, a[0].Length)) { return; }
        if (a[r][c] == '1' || a[r][c] == 'X') { return; }

        a[r][c] = '1';

        // dfs up, down, left, right...respectively
        DepthFirstSearch(a, r - 1, c);
        DepthFirstSearch(a, r + 1, c);
        DepthFirstSearch(a, r, c - 1);
        DepthFirstSearch(a, r, c + 1);
    }

    // assume n x n matrix ???
    // assume board will contain
    // ONLY 'X's and 'O's
    // SIDE NOTE: May or may not an N X N matrix
    public void Solve(char[][] a)
    {
        if (a.Length == 0) { return; }

        int numRows = a.Length;
        int numColumns = a[0].Length;

        // DFS first & last row
        for (int col = 0; col < numColumns; ++col)
        {
            if (a[0][col] == 'O')
            {
                a[0][col] = '1';
                DepthFirstSearch(a, 1, col);
            }

            if (a[numRows - 1][col] == 'O')
            {
                a[numRows - 1][col] = '1';
                DepthFirstSearch(a, numRows - 2, col);
            }
        }

        // DFS first and last columns
        for (int row = 0; row < numRows; ++row)
        {
            if (a[row][0] == 'O')
            {
                a[row][0] = '1';
                DepthFirstSearch(a, row, 1);
            }

            if (a[row][numColumns - 1] == 'O')
            {
                a[row][numColumns - 1] = '1';
                DepthFirstSearch(a, row, numColumns - 2);
            }
        }

        // turn all 'O's to 'X's
        // turn all '1's to 'O's
        for (int i = 0; i < numRows; ++i)
        {
            for (int j = 0; j < numColumns; ++j)
            {
                if (a[i][j] == '1')
                {
                    a[i][j] = 'O';
                }
                else if (a[i][j] == 'O')
                {
                    a[i][j] = 'X';
                }
            }
        }
    }
}
