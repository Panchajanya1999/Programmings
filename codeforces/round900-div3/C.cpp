// C. Vasilije in Cacak
// Link: https://codeforces.com/contest/1878/problem/C

#include <bits/stdc++.h>
using namespace std;

int32_t main() {
    auto sumn = [&] (int n) -> long long{
        return 1LL *  n * (n + 1) / 2;
    };
    int n, k, t = 1;
    cin >> t;
    while (t > 0)
    {
        /* code */
        long long x;
        cin >> n >> k >> x;  

        long long minsum = sumn(k);
        long long maxsum = sumn(n) - sumn(n - k);

        if (x >= minsum && x <= maxsum) {
            cout << "YES" << '\n';
        }
        else {
            cout << "NO" << '\n';
    }
    t--;
    }
    return 0;
}