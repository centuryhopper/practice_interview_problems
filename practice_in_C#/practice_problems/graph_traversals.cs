using System.Collections;
using System.IO;
using System;
using System.Collections.Generic;


namespace GraphTraversals
{
    public struct Graph
    {
        bool[,] matrix;
        public int matrixSize;

        /// <summary>
        /// read in text file to populate
        /// adjacency matrix
        /// </summary>
        /// <param name="filename"></param>
        public Graph(string filename)
        {
            if (!File.Exists(filename))
            {
                System.Console.WriteLine(("error: file does not exist"));
                Environment.Exit(0);
            }

            using (StreamReader reader = new StreamReader(filename))
            {
                Int32.TryParse(reader.ReadLine(), out matrixSize);
                // System.Console.WriteLine(matrixSize);

                this.matrix = new bool[matrixSize, matrixSize];

                for (int row = 0; row < matrixSize; ++row)
                {
                    string line = reader.ReadLine();
                    string[] pieces = line.Split(' ');

                    // pieces length and matrix size should be the same
                    for (int column = 0; column < pieces.Length; ++column)
                    {
                        string spaceOrEmpty = column == pieces.Length - 1 ? string.Empty : " ";
                        this.matrix[row, column] = pieces[column] == "1";
                        // System.Console.Write(matrix[row, column] + spaceOrEmpty);
                    }

                    // System.Console.WriteLine();
                }
            }
        }

        public void dfs(int node, bool[] visited)
        {
            // stack algorithm
            Stack<int> s = new Stack<int>();

            // mark node as visited and add it to the stack
            s.Push(node);
            visited[node] = true;

            // pop each element accordingly for breadth first search to work
            // loop thru matrix as the way to traverse the graph
            while (s.Count > 0)
            {
                int elem = s.Pop();
                System.Console.WriteLine(elem);

                // loop thru columns
                for (int i = 0; i < matrixSize; ++i)
                {
                    // if it's adjacent to our current elem and we haven't visited
                    // it before
                    if (matrix[elem, i] && !visited[i])
                    {
                        // anything push into the stack has
                        // to be marked as visited
                        s.Push(i);
                        visited[i] = true;
                    }
                }
            }
        }

        public void dfs(int startingNode)
        {
            // initialize visited array
            // and run dfs(int, bool[])

            System.Console.WriteLine("depth-first search:");
            bool[] visited = new bool[matrixSize];
            dfs(startingNode, visited);
        }

        public void bfs(int startingNode)
        {
            System.Console.WriteLine("breadth-first search:");
            bool[] visited = new bool[matrixSize];
            bfs(startingNode, visited);
        }

        public void bfs(int node, bool[] visited)
        {
            // queue algorithm

            Queue<int> q = new Queue<int>();
            q.Enqueue(node);
            visited[node] = true;

            while (q.Count > 0)
            {
                int elem = q.Dequeue();
                System.Console.WriteLine(elem);

                // loop thru each column and add it to the queue
                for (int i = 0; i < matrixSize; ++i)
                {
                    if (!visited[i] && matrix[elem, i])
                    {
                        q.Enqueue(i);
                        visited[i] = true;
                    }
                }
            }
        }

    }
}
