#include<bits/stdc++.h>
using namespace std;
const int N = 1e3;
int arr[N][N];
int sum[N][N];
int main(){
    int n, q;
    scanf("%d",&n);
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=n; j++) {
            scanf("%d",&arr[i][j]);
            sum[i][j] = arr[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1];
        }
    }
    scanf("%d",&q);
    int x1, x2, y1, y2;

    while(q--){
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        int ans = sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1];
        cout << ans << endl;
    }



//    for(int i=1; i<=n; i++) {
//        for(int j=1; j<=n; j++) {
//            printf("%d ",arr[i][j]);
//        }
//        cout << endl;
//    }
}
