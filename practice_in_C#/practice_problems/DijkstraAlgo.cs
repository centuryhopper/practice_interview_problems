using System;
using System.Collections;
using System.Collections.Generic;
using data_structures;
using System.IO;

namespace PathFinding
{
    using PriorityQueue = PriorityQueue<Vertex>;

    public struct Vertex
    {
        public int id;

        /// <summary>
        /// AKA G-cost for A* algorithm
        /// </summary>
        public int distanceCost;

        public Vertex(int id, int dist)
        {
            this.id = id;
            this.distanceCost = dist;
        }

        override public String ToString()
        {
            return "Cost of shortest path to vertex " + (char)(this.id + 'A') + ": " + this.distanceCost;
        }
    }

    public class DijkstraAlgo
    {
        private int[,] matrix;
        int n;
        const int oo = (int)1e9;

        // Initialize 2D 'matrix' from input file.
        public DijkstraAlgo(string filename)
        {
            StreamReader r = new StreamReader(filename);

            n = Convert.ToInt32(r.ReadLine());

            matrix = new int[n, n];

            for (int i = 0; i < n; i++)
            {
                string line = r.ReadLine();
                string[] vertices = line.Split(' ');
                for (int j = 0; j < n; j++)
                {
                    // string spaceOrEmpty = j == vertices.Length - 1 ? String.Empty : " ";
                    // Console.Write(vertices[j] + spaceOrEmpty);
                    matrix[i, j] = Convert.ToInt32(vertices[j]);
                    // Console.Write(matrix[i, j] + spaceOrEmpty);
                }
                p("");
            }

            // PrintMatrix();

            r.Close();
        }

        private void PrintMatrix()
        {
            p("");
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Console.Write(matrix[i, j] + " ");
                }
                p("");
            }
        }

        // Prints the length of the shortest path from 'source' to each other vertex
        // in the graph. Assumes non-negative edge weights.
        public void RunDijkstra(int source)
        {
            int [] dist = new int[n];
            bool [] visited = new bool[n];
            int numVisited = 0;

            // sort the minheap based off of vertex distance cost values
            var minheap = new PriorityQueue(2 * n, false, (Vertex v1, Vertex v2) => v1.distanceCost.CompareTo(v2.distanceCost));

            // every vertex will have a default cost of oo
            Array.Fill(dist, oo);

            // mark starting vertex
            dist[source] = 0;

            for (int i = 0; i < n; i++)
                minheap.Enqueue(new Vertex(i, dist[i]));

            // minheap.PrintQueue();
            p("");

            // PrintMatrix();

            while (!minheap.IsEmpty && numVisited < n)
            {
                // Find the vertex with the smallest distance associated with it.
                Vertex v = minheap.Dequeue();
                if (visited[v.id]) continue;

                visited[v.id] = true;
                p(v);
                ++numVisited;

                // todo checks all possible nodes in the graph
                // todo which means we'll run into v's neighbor nodes eventually
                for (int i = 0; i < n; i++)
                {
                    // Note: Checking for !visited[i] here is actually not necessary. Can you see why?
                    // todo it's not necessary because any node marked as visited is already distance-optimized

                    // todo "matrix[v.id][i] > 0" will be used to check for neighboring nodes, positive means
                    // there is an edge, negative means there's not direct edge
                    if (matrix[v.id, i] > 0 && !visited[i] && dist[v.id] + matrix[v.id, i] < dist[i])
                    {
                        // This is a bit lazy. A vertex might be thrown into the
                        // heap multiple times. This is a fairly cheap operation,
                        // though, and the duplicates don't affect our solution
                        // because the ones with higher dist values will be
                        // suppressed, while the once with lower dist values will
                        // percolate to the top of the heap. Once each vertex has
                        // been visited, we'll just stop coming into the while-loop,
                        // and all those duplicates will be ignored.

                        dist[i] = dist[v.id] + matrix[v.id, i];
                        minheap.Enqueue(new Vertex(i, dist[i]));
                    }
                }
            }

            if (numVisited != n)
                p("Oh no! You fed a disconnected graph to Dijkstra!");
        }

        private void p(object m) => Console.WriteLine(m);

    }
}