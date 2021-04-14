#include <bits/stdc++.h>


// assume array is sorted
int recursive_binary_search(int* ar, int targetVal, int lo, int hi)
{
    if (lo >= hi) return -1;
    int mid = lo + ((hi - lo) / 2);
    if (ar[mid] < targetVal)
        return recursive_binary_search(ar, targetVal, mid+1, hi);
    if (ar[mid] > targetVal)
        return recursive_binary_search(ar, targetVal, lo, mid-1);
    return mid;
}

int bin_search(int* array, int n, int targetVal)
{
    return recursive_binary_search(array, targetVal, 0, n-1);
}


int main(int argc, char const *argv[])
{
    int ar[] = {6,7,8,10,46,75,7,9,5,4};
    int n = sizeof(ar) / sizeof(int);

    // for (int i = 0; i < n; i++)
    //     ar[i] = rand() % 11;
    std::sort(std::begin(ar), std::end(ar));
    printf("after sorting\n");
    for (int i = 0; i < n; i++)
        std::cout << ar[i] << " ";
    printf("\n");

    printf("value found at index %d\n", bin_search(ar, n, 10));
    return 0;
}



