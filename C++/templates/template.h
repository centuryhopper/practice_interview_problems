#pragma once
// originally from https://github.com/rachitiitr/DataStructures-Algorithms/blob/master/Library/Miscellanious/template.cpp
#include <bits/stdc++.h>
using namespace std;
#define nl cout<<endl;
#define gc getchar_unlocked
#define fo(i, n) for (i = 0; i < n; i++)
#define Fo(i, k, n) for (i = k; k < n ? i < n : i > n; k < n ? i += 1 : i -= 1)
#define ll long long
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define ss(s) scanf("%s", s)
#define pi(x) printf("%d\n", x)
#define pl(x) printf("%lld\n", x)
#define ps(s) printf("%s\n", s)
#define deb(x) cout << #x << " = " << x << ", ";nl;
#define deb2(x, y) cout << #x << " = " << x << "," << #y << " = " << y << endl
#define pb push_back
#define eb emplace_back
#define null NULL
#define mp make_pair
#define F first
#define S second
#define clr(x) memset(x, 0, sizeof(x))
#define tr(it, a) for (auto it = a.begin(); it != a.end(); it++)
#define ts to_string
#define all(x) x.begin(), x.end()
#define sortall(x) sort(all(x))
#define p(v) for_each(all(v), [](auto e) { cout<<e<<" "; })
#define PI 3.1415926535897932384626
#define map(from,to,f) transform(all(from),to.begin(),f)
typedef pair<int, int> pii;
typedef pair<ll, ll> pl;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vpii;
typedef vector<pl> vpl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef unordered_map<int,int> umii;
mt19937_64 rang(chrono::high_resolution_clock::now().time_since_epoch().count());
int rng(int lim)
{
    uniform_int_distribution<int> uid(0, lim - 1);
    return uid(rang);
}



