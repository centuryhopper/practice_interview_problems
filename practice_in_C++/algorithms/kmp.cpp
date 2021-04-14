#include <bits/stdc++.h>
#define null NULL

// O(n^2)
// heap allocated
// int *lps_preprocess(const std::string& pat)
// {
//     int n = pat.length();
//     int* lps = (int*) calloc(n, sizeof(int));
//     int i = 0, j = 1;

//     while (j < n)
//     {
//         // mismatch
//         if (pat[i] != pat[j])
//         {
//             // map i back to the value at its previous index
//             if (i != 0)
//             {
//                 i = lps[i - 1];
//             }
//             else
//             {
//                 lps[j++] = 0;
//             }
//         }
//         // match
//         else
//         {
//             lps[j] = i + 1;
//             ++j; ++i;
//         }
//     }

//     return lps;
// }

// O(n^2)
// stack allocated as opposed to heap
void lps_preprocess(const std::string& pat, int* lps)
{
    int n = pat.length();
    lps[0] = 0;
    int i = 0, j = 1;

    while (j < n)
    {
        // mismatch
        if (pat[i] != pat[j])
        {
            // map i back to the value at its previous index
            if (i != 0)
            {
                i = lps[i - 1];
            }
            else
            {
                lps[j++] = 0;
            }
        }
        // match
        else
        {
            lps[j] = i + 1;
            ++j; ++i;
        }
    }
}

void kmp(const std::string& text, const std::string& pat)
{
    int m = text.length(), n = pat.length();
    int lps[n];
    lps_preprocess(pat, lps);
    for (int i = 0; i < n; ++i)
        std::cout << lps[i] << " ";
    printf("\n");
    int i = 0, j = 0;

    while (i < m)
    {
        if (text[i] == pat[j])
        {
            ++i;
            ++j;
        }

        // j has traversed the entire pattern string, so map it back to the value at its previous index
        if (j == n)
        {
            printf("pattern found at index %d\n", i - j);
            // map j back to the value at its previous index
            j = lps[j - 1];
        }

        // mismatch
        else if (i < m && text[i] != pat[j])
        {
            if (j != 0)
            {
                j = lps[j - 1];
            }
            else
            {
                ++i;
            }
        }
    }
}


int main(int argc, char const *argv[])
{
    // std::string text = "ababcabcabababd", pattern = "ababd";
    // std::string text = "ababcabcabababd", pattern = "ababd";
    std::string text = "ABABDABACDABABCABAB", pattern = "ABABCABAB";

    kmp(text, pattern);
    // std::cout << "hello" << std::endl;

    return 0;
}
