using System;
using GraphTraversals;
using sorting_algos;

namespace practice_problems
{
    class Program
    {
        static void print(object msg = null) => System.Console.WriteLine(msg);
        static void Main(string[] args)
        {
            print("");
            // Graph g = new Graph("graph.txt");
            // g.dfs(0);
            // g.bfs(0);

            int[] array = new int[] { 5, 4, 3, 2, 1, 0 };
            SortingAlgos s = new SortingAlgos();
            s.MergeSort(array);

            s.PrintArray(array);

            print("");
        }
    }
}
