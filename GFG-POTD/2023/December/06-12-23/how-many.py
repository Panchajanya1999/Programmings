//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
public:
    int count(int a, int x) {
        int count = 0;
        while (a > 0) {
            if (a % 10 == x)
                count++;
            a /= 10;
        }
        return count;
    }

    int countX(int L, int R, int X) {
        int ans = 0;
        for (int i = L+1; i < R; i++) {
            ans += count(i, X);
        }
        return ans;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int L, R, X;
        cin >> L >> R >> X;
        Solution ob;
        int ans = ob.countX(L, R, X);
        cout << ans << "\n";
    }
}

// } Driver Code Ends
