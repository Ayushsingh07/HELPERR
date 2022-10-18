#include<bits/stdc++.h>
using namespace std;
signed main()
{
    int n; cin>>n;
    vector<int> v(n);
    for(int i=0; i<=n-1; i++){
        cin>>v[i];
    }
    for(int i=0; i<n; i++){
        int curr = v[i];
        int j=i-1;
        while(j>=0 && curr<v[j]){
            v[j+1] = v[j];
            j--;
        }
        v[j+1] = curr;
    }
    for(int i=0; i<n; i++){
        cout<<v[i]<<" ";
    }
    return 0;
}
