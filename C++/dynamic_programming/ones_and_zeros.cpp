









//         unordered_map<string, pair<int,int>> map;

//         // count number of 0's and 1's in each string
//         for (string s : lst)
//         {
//             int zeros = std::count(s.begin(), s.end(), '0');
//             int ones = std::count(s.begin(), s.end(), '1');
//             map[s] = {zeros, ones};
//         }

//         for (auto e : map)
//         {
//             string key = e.first;
//             int zeros = e.second.first;
//             int ones = e.second.second;
//             cout << key << ": " << zeros << ", " << ones << "\n";

//         }


//         int dp[m+1][n+1];
//         memset(dp, 0, sizeof(dp));

//         // fill first row
//         for (int i = 0; i <= n; ++i)
//         {
//             int cnt = 0;
//             for (auto e : map)
//             {
//                 string key = e.first;
//                 int zeros = e.second.first;
//                 int ones = e.second.second;
//                 // cout << key << ": " << zeroes << ", " << ones << "\n";
//                 // count all strings with no ones and less than or equal to i
//                 if (zeros == 0 && ones <= i)
//                 {
//                    cnt++;
//                 }
//             }
//             dp[0][i] = cnt;
//         }

//         // fill columns
//         for (int i = 0; i <= m; ++i)
//         {
//             int cnt = 0;
//             for (auto e : map)
//             {
//                 string key = e.first;
//                 int zeros = e.second.first;
//                 int ones = e.second.second;
//                 // cout << key << ": " << zeroes << ", " << ones << "\n";
//                 // count all strings with no ones and less than or equal to i
//                 if (ones == 0 && zeros <= i)
//                 {
//                    cnt++;
//                 }

//             }
//             dp[i][0] = cnt;
//         }

// //         for (int i = 0; i <= m; ++i)
// //         {
// //             for (int j = 0; j <= n;++j)
// //             {
// //                 cout << dp[i][j] << " ";
// //             }
// //             cout << "\n";

// //         }

//         for (int i = 1; i <= m; ++i)
//         {
//             for (int j = 1; j <= n; ++j)
//             {
//                 int res;
//                 int aboveMe = dp[i-1][j];
//                 int leftOfMe = dp[i][j-1];
//                 if (aboveMe == leftOfMe)
//                 {
//                     res = dp[i-1][j] + 1;
//                 }
//                 else
//                 {
//                     res = max(aboveMe, leftOfMe);
//                 }

//                 dp[i][j] = res;
//             }

//         }

//         return dp[m][n];