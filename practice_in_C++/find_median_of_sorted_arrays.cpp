#include <cstdint>
#include <iostream>
#include <thread>
#include <vector>
#include <atomic>
#include <chrono>
#include <string>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <climits>
#include <iterator>
#include <queue>
#include <sstream>
#define print(x) std::cout << x << std::endl
using namespace std;

// g++ –std=c++17 [filename].cpp && ./a.out (type '–std=c++17' out manually. Don't copy
// & paste because the copy & pasted hyphen isn't recognized)


/*

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000


*/


// read-only
double FindMedianOfArray(const std::vector<int>& array)
{
    int len = array.size();
    if (len % 2 == 1)
    {
        return array[len / 2];
    }
    else
    {
        int fl = len / 2 , cl = (len / 2) - 1;
        return static_cast<double>(array[fl] + array[cl]) / 2;
    }
}

double findMedianSortedArrays(std::vector<int> &a, std::vector<int> &b)
{
    // both are empty
    int aLen = a.size(), bLen = b.size();
    if (aLen == 0 && bLen == 0) { return 0; }
    if (aLen == 0) { return FindMedianOfArray(b); }
    if (bLen == 0) { return FindMedianOfArray(a); }

    vector<int> mergedArray;

    // preallocate size
    mergedArray.reserve(aLen + bLen);

    mergedArray.insert(mergedArray.end(), a.begin(), a.end());

    mergedArray.insert(mergedArray.end(), b.begin(), b.end());

    std::sort(mergedArray.begin(), mergedArray.end());

    return FindMedianOfArray(mergedArray);
}

#pragma region
// assumes both array inputs are sorted
// double findMedianSortedArrays(std::vector<int> &a, std::vector<int> &b)
// {
//     // both are empty
//     int aLen = a.size(), bLen = b.size();
//     if (aLen == bLen == 0) { return 0; }

//     vector<int> mergedArray(aLen + bLen);

//     // algorithm here:
//     int first = 0, second = 0;

//     // compare and start merging
//     while (first < aLen && second < bLen)
//     {
//         if (a[first] < b[second])
//         {

//         }
//     }

//     // at least one of the two arrays is done
//     // so we copy in the rest of the elements into the merged array

//     // if first > a length --> while loop copy b contents over

//     // if second > b length --> while loop copy a contents over

//     // find the median value of the merged array




//     return 0;
// }
#pragma endregion

int main(int argc, char const *argv[])
{
    std::cout << std::boolalpha << std::endl;

    vector<int> a {};
    vector<int> b {1};

    // int data[5] = {0};

    print(findMedianSortedArrays(a, b));

    return 0;
}
