using System;


public class SetMatrixZeroes
{
    void p(object m) => Console.WriteLine(m);

    public void SetZeroes(int[][] matrix)
    {
        int numRows = matrix.Length;
        int numColumns = matrix[0].Length;

        bool does_first_row_have_a_zero = false;

        // loop thru first row
        for (int j = 0; j < numColumns; ++j)
        {
            if (matrix[0][j] == 0)
            {
                does_first_row_have_a_zero = true;
                break;
            }
        }

        // loop thru entire matrix (first matrix pass)
        // mark for columns to remember for later
        for (int i = 0; i < numRows; ++i)
        {
            for (int j = 0; j < numColumns; ++j)
            {
                if (matrix[i][j] == 0)
                {
                    // set the first row's
                    // jth column to 0
                    matrix[0][j] = 0;
                }
            }
        }

        // second matrix pass
        for (int i = 1; i < numRows; ++i)
        {
            bool contains_zero = false;
            for (int j = 0; j < numColumns; ++j)
            {
                // find our zero and leave early
                if (matrix[i][j] == 0)
                {
                    contains_zero = true;
                    break;
                }
            }

            // check columns of each row
            // -contains_zero will help determine whether
            // a neighbor on the same row is 0
            // -whether matrix[0][j] is 0 or not will determine
            // whether the jth column should be 0
            // because the first row will be used as a reference (no pun intended)
            for (int j = 0; j < numColumns; ++j)
            {
                if (contains_zero || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }

        // make sure we zero out the first row
        if (does_first_row_have_a_zero)
        {
            // fill the first row with 0s
            Array.Fill(matrix[0], 0);
        }
    }
}