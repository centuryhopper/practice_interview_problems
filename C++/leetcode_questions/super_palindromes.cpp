#include "../templates/template.h"

class Solution
{

public:
    int superpalindromesInRange(string left, string right)
    {
        int cnt = 0;
        int size1 = left.length(), size2 = right.length();
        ll l = stoll(left), r = stoll(right);

        // odd case (12345 -> 4321    for 1234X4321, where 0 <= X <= 9)
        for (int i = 0; i < 100'000; ++i)
        {
            // get string and its palindrome
            string s1 = ts(i);
            string s2 = s1;
            // reverse(s2.begin(), s2.end()-1);

            // cout<<s1 <<" " <<s2<<endl;

            string s = s1;
            for (auto it = s2.rbegin()+1; it != s2.rend();++it)
            {
                s += *it;
            }

            // cout<<s<<endl;
            ll num = stoll(s);
            num *= num;

            if (num > r) break;

            string squared = ts(num);

            if (num >= l && squared == string(squared.rbegin(), squared.rend()))
            {
                // cout<<num<<endl;
                cnt += 1;
            }
        }

        printf("\n");

        // even case (12345 -> 54321    for 1234554321)
        for (int i = 0; i < 100'000; ++i)
        {
            // get string and its palindrome
            string s1 = ts(i);
            string s2 = s1;
            string s = s1;
            for (auto it = s2.rbegin(); it != s2.rend();++it)
            {
                s += *it;
            }
            ll num = stoll(s);
            num *= num;

            // cout<<num<<endl;
            if (num > r) break;

            string squared = ts(num);

            if (num >= l && squared == string(squared.rbegin(), squared.rend())) cnt += 1;
        }


        return cnt;
    }
};


pair<bool,ll> isPerfectSquare(ll n)
{
    ll squareRootN = (ll)round((sqrt(n)));
    cout<<squareRootN<<endl;
    return {squareRootN*squareRootN == n, squareRootN};
}




int main(int argc, const char **argv)
{

    return 0;
}

#pragma region optimized online solution
/*
class Solution {
public:
    int superpalindromesInRange(string L, string R) {
        long double lb = sqrtl(stol(L));
        long double ub = sqrtl(stol(R));

        int ans = lb <= 3 && 3 <= ub;

        queue<pair<long, int>> q;
        q.push({1, 1});
        q.push({2, 1});

        while (true) {
            auto p = q.front();
            q.pop();
            long x = p.first, len = p.second;

            if (x > ub)
                break;

            long W = powl(10, (len + 1) / 2);
            if (x >= lb)
                ans += is_palindrome(x * x);

            long r = x % W, l = x - (len % 2 ? x % (W / 10) : r);

            if (len % 2)
                q.push({10 * l + r, len + 1});
            else
                for (int d = 0; d <= 2; d++)
                    q.push({10 * l + d * W + r, len + 1});
        }

        return ans;
    }
private:
    bool is_palindrome(long x) {
        if (x == 0) return true;
        if (x % 10 == 0) return false;
        long left = x, right = 0;
        while (left >= right) {
            if (left == right || left / 10 == right) return true;
            right = 10 * right + (left % 10), left /= 10;
        }
        return false;
    }
};
*/
#pragma endregion


/*
#define ll long long
#define ts to_string
#define all(v) v.begin(),v.end()
#define pb push_back

class Solution
{
private:
    ll getPalin(ll num)
    {
        vector<ll> v;

        while (num > 0)
        {
            v.pb(num%10);
            num/=10;
        }

        ll ret = 0, n = v.size();
        for (int i=0;i<n;++i)
        {
            ret += v[i] * pow(10,n-1-i);
        }

        return ret;
    }


public:
    int superpalindromesInRange(string left, string right)
    {
        int cnt = 0;
        ll l = sqrt(stoll(left)), r = sqrt(stoll(right));

        for (ll i = l;i <= r;++i)
        {
            // ll palin = getPalin(i);
            string og = ts(i);
            string rev = og;
            reverse(all(rev));

            // sqrt of number check
            if (rev != og) continue;
            // cout<<i<<", "<<palin<<endl;

            // check square number palindrome
            og = ts(i*i);
            rev = og;
            reverse(all(rev));

            if (rev != og) continue;

            // cout<<i<<", "<<sq<<endl;
            ++cnt;
        }


        // string h = "hello";
        // string t = h;
        // reverse(all(h));
        // cout<<getPalin(4343)<<endl;

        return cnt;
    }
};
*/



/*
#define ll long long
#define ts to_string
#define all(v) v.begin(),v.end()
#define pb push_back

class Solution
{

public:
    int superpalindromesInRange(string left, string right)
    {
        int cnt = 0;
        int size1 = left.length(), size2 = right.length();
        ll l = stoll(left), r = stoll(right);

        // odd case (12345 -> 4321    for 1234X4321, where 0 <= X <= 9)
        for (int i = 0; i < (int)1e5; ++i)
        {
            // get string and its palindrome
            string s1 = ts(i);
            string s2 = s1;
            reverse(s2.begin(), s2.end()-1);

            // handles single digits
            if (s2.length() == 1) s2 = "";
            // cout<<s1 <<" " <<s2<<endl;

            string s = s1 + s2;
            // cout<<s<<endl;
            ll num = pow(stoll(s), 2);

            if (num > r) break;

            string squared = ts(num);
            string palin = string(squared.rbegin(), squared.rend());

            cout<< (squared == palin) <<endl;


            if (num >= l && squared == string(squared.rbegin(), squared.rend()))
            {
                cout<<num<<endl;
                cnt += 1;
            }

        }

        printf("\n");

        // even case (12345 -> 54321    for 1234554321)
        for (int i = 0; i < (int)1e5; ++i)
        {
            // get string and its palindrome
            string s1 = ts(i);
            string s2 = s1;
            reverse(s2.begin(), s2.end());
            // cout<<s1 <<" " <<s2<<endl;

            string s = s1 + s2;
            ll num = pow(stoll(s), 2);
            // cout<<num<<endl;
            if (num > r) break;

            string squared = ts(num);

            if (num >= l && squared == string(squared.rbegin(), squared.rend())) cnt += 1;
        }


        return cnt;
    }
};

*/