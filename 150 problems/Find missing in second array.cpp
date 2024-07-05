#include <bits/stdc++.h>
using namespace std;

vector<int> findMissing(int a[], int b[], int n, int m)
{
    map<long, int> mp;
    for(int i = 0; i < m; i++) {
        mp[b[i]] = 1;
    }

    vector<int> ans;
    for(int i = 0; i < n; i++) {
        if(mp.find(a[i]) == mp.end()) {
            ans.push_back(a[i]);
        }
    }

    return ans;
}

int main()
{
    int n, m;

    cin >> n;
    int a[n];
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }

    cin >> m;
    int b[m];
    for(int i = 0; i < m; i++) {
        cin >> b[i];
    }

    vector<int> result = findMissing(a, b, n, m);
    for(int i : result) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
