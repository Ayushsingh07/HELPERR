// DNF Sort ALso known as Dutch National Flag Problem
// In this an array of 0's, 1's and 2's will be given , we have to sort the array in O(log(n))
#include<bits/stdc++.h>
using namespace std;
void dnfsort(vector<int> &v, int n){
    int i=0, j=0, k=n-1;
    while(j<=k){
        if(v[j]==0){
            swap(v[i],v[j]);
            i++; j++;
        }
        else if(v[j]==1){
            j++;
        }
        else if(v[j]==2){
            swap(v[j],v[k]);
            k--;
        }
    }
}
signed main()
{
    int n; cin>>n;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    dnfsort(v,n);
    for(int i=0; i<n; i++){
        cout<<v[i]<<" ";
    }
    return 0;
}