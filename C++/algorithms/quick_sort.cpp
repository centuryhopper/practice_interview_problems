#include "../templates/template.h"
#include <ctime>

struct QuickSort
{
    int partitionIndex(int *arr, int lo, int hi)
    {
        int leftPtr = lo, rightPtr = hi, pivot = lo;
        while (leftPtr < rightPtr)
        {

            // i < hi to prevent i from going out of bounds in the case that i starts at the highest value
            while (arr[leftPtr] <= arr[pivot] && leftPtr < hi)
                ++leftPtr;
            // if (arr[pivot] == 6)
            // {
            //     deb2(arr[leftPtr], arr[rightPtr]);
            //     nl;
            //     for (int i = 0; i <= hi; i++) cout<< arr[i] << ' ';
            //     nl;
            // }

            while (arr[rightPtr] > arr[pivot])
                --rightPtr;

            // we make sure i and j cross by doing so
            if (leftPtr < rightPtr)
                swap(arr[leftPtr], arr[rightPtr]);
        }

        // swap right pointer with pivot
        swap(arr[rightPtr], arr[pivot]);


        return rightPtr;
    }

    void quickSort(int *arr, int lo, int hi)
    {
        if (lo >= hi)
            return;

        int p = partitionIndex(arr, lo, hi);
        // left of p and right of p are not sorted
        quickSort(arr, lo, p - 1);
        quickSort(arr, p + 1, hi);
    }
};

void sort(QuickSort &s, int *ar, int n)
{
    s.quickSort(ar, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << ar[i] << ' ';
    }
    nl;
}

int main(int argc, char const *argv[])
{
    QuickSort s;
    int ar[] = {3, 2, 1, 4, 6, 5};
    int ar2[] = {10, 15, 1, 2, 9, 16, 11};
    int ar3[] = {7, 6, 10, 5, 9, 2, 1, 15, 7};
    int ar4[] =
        {
            78,
            37,
            76,
            24,
            51,
            76,
            17,
            67,
            28,
            24,
            66,
            1,
            47,
            87,
            73,
            15,
            73,
            31,
            29,
            72,
            4,
            49,
            58,
            74,
            94,
        };

    clock_t start = clock();
    sort(s, ar, sizeof(ar) / sizeof(int));
    nl;
    cout<<(clock() - start) / CLOCKS_PER_SEC<<endl;
    // sort(s, ar2, sizeof(ar2) / sizeof(int));
    // nl;
    // sort(s, ar3, sizeof(ar3) / sizeof(int));
    // nl;
    // sort(s, ar4, sizeof(ar4) / sizeof(int));

    return 0;
}
