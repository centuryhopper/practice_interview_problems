#include <cstdint>
#include <exception>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <iterator>
#include <array>
#include <vector>
#include <map>
#include <set>
#include <tuple>
#include <stack>
#include <queue>
#include <cstdlib>
#define print(x) std::cout << x << std::endl;
#define fl(i, k, n) for (int i = k; i < n; ++i)
using namespace std;


class Graph
{
    public:
        Graph(std::string filename);
        ~Graph();

        // runner method
        void dfs();
        void dfs(int, bool**);

        bool** matrix;
        int matrixSize;
};

Graph::Graph(string filename)
{
    // read in text file to populate adjacency matrix
    std::ifstream reader(filename);


    try
    {
        if (!reader.is_open())
        {
            throw 0;
        }
        else
        {
            print("file opened");
        }
    }
    catch(...)
    {

        print("file does not exist!!!");
        exit(1);
    }



    // get the first line and parse into int
    string txt = "";
    getline(reader, txt);
    matrixSize = txt == "" ? 0 : stoi(txt);
    // print(matrixSize);


    // allocate matrixSize x matrixSize 2D array
    this->matrix = new bool*[matrixSize];

    for (int row = 0; row < matrixSize; ++row)
    {
        // allocate each cell with a bool array
        this->matrix[row] = new bool[matrixSize];

        // read one line at a time
        getline(reader, txt);

        #pragma region split the string up into a string array
        string lst[matrixSize];
        int t = 0;
        stringstream st(txt);
        while(st.good() && t < matrixSize)
        {
            st >> lst[t++];
        }

        #pragma region debug check
        // for (int i = 0; i < matrixSize; i++)
        // {
        //     print(lst[i]);
        // }
        // print("")
        #pragma endregion



        #pragma endregion

        // populate with bool values
        for (int col = 0; col < matrixSize; ++col)
        {
            this->matrix[row][col] = lst[col] == "1";
            print(this->matrix[row][col]);
        }
        print("")
    }


    // string line = "test one two three.";
    // string arr[4];
    // int i = 0;
    // stringstream ssin(line);
    // while (ssin.good() && i < 4){
    //     ssin >> arr[i];
    //     ++i;
    // }
    // for(i = 0; i < 4; i++){
    //     cout << arr[i] << endl;
    // }



    reader.close();

}

Graph::~Graph()
{
    // deallocate each array inside
    for (int i = 0; i < matrixSize; ++i)
        delete[] this->matrix[i];

    // then deallocate the whole 2D array
    delete [] this->matrix;
}



int main(int argc, char const *argv[])
{
    std::cout << std::boolalpha << std::endl;

    Graph g("graph2.txt");

    return 0;
}
