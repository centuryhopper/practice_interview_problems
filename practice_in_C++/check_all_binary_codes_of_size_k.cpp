#include <iostream>
#include <set>
#include <cmath>

using namespace std;

class Solution {
public:

    void p(int x) {  std::cout << x << "\n"; }

    bool hasAllCodes(string s, int k)
    {
        int n = s.size();
        if (k > n) return false;

        set<string> set;
        for (int i = k-1; i < n; i++)
        {
            // substr's 2nd parameter is the number of characters ahead of (i-k+1)
            string tmp = s.substr(i-k+1,k);
            // cout << i-k+1 << ',' << i << " for " << tmp << "\n";
            set.insert(tmp);
        }

        for (auto i : set)
        {
            cout << i << "\n";
        }

        return set.size() == pow(2, k);
    }
};





#pragma region Interesting online solution
// class Solution {
// public:
// 	bool hasAllCodes(string& s, int k) {

//         if (k>15) return false;

// 		bool set[1<<k];
//         memset(set, 0, sizeof(set));

// 		int n = stoi(s.substr(0,k), 0, 2);
// 		for (int i=k; i <= s.size(); i++) {
// 			// check prev window
// 			set[n] = true;
// 			if (i == s.size()) break;
//             n = n & ~(1 << (k-1)); // clear kth bit
// 			n = (n << 1) | (s[i]-'0');
// 		}

//         for (int i=0; i < (1<<k); i++)
//             if (set[i] == false) return false;

// 		return true;
// 	}

// };

// static auto _______ = [](){
// 	std::ios::sync_with_stdio(false);
// 	std::cin.tie(NULL);
// 	std::cout.tie(NULL);
// 	return 0;
// }();
#pragma endregion

