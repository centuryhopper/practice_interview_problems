using System;
using GraphTraversals;
using sorting_algos;
using data_structures;

namespace practice_problems
{
    // type-aliasing for simplified typing
    using PriorityQueue = DataStructures.PriorityQueue<int>;
    class Program
    {
        static void p(object msg = null) => System.Console.WriteLine(msg);
        static void Main(string[] args)
        {
            p("");
            // Graph g = new Graph("graph.txt");
            // g.dfs(0);
            // g.bfs(0);

            // int[] array = new int[] { 5, 4, 3, 2, 1, 0 };
            // SortingAlgos s = new SortingAlgos();
            // s.MergeSort(array);

            // s.PrintArray(array);

            PriorityQueue pq = new PriorityQueue(true);

            for (int i = 1; i <= 10; i++)
            {
                pq.Enqueue(i);
            }

            p("size: " + pq.size);

            p("");
            pq.Enqueue(0);
            pq.PrintQueue();
            p("size: " + pq.size);
            p("");

            p("");
            pq.Dequeue();
            pq.PrintQueue();
            p("size: " + pq.size);
            p("");

            p("");
            // pq.Dequeue();
            // pq.PrintQueue();
            // p("size: " + pq.size);
            p("");

            // for (int i = 0; i < 9; i++)
            // {
            //     pq.Dequeue();
            //     pq.PrintQueue();
            //     p("size: " + pq.size);
            // }
        }
    }
}

