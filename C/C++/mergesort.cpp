#include<bits/stdc++.h>
using namespace std;
void merge(vector<int> &v, int l, int r, int mid){
    int i = l;
    int j = mid+1;
    int k = l;
    vector<int> temp(r+1);
    while(i<=mid && j<=r){
        if(v[i]<v[j]){
            temp[k] = v[i];
            i++;
        }
        else{
            temp[k] = v[j];
            j++;
        }
        k++;
    }
    while(i<=mid){
        temp[k] = v[i];
        k++;
        i++;
    }
    while(j<=r){
        temp[k] = v[j];
        k++;
        j++;
    }
    for(int i=l; i<=r; i++){
        v[i] = temp[i];
    }
}
void mergeSort(vector<int> &v, int l, int r){
    if(l<r){
        int mid = (l+r)/2;
        mergeSort(v,0,mid);
        mergeSort(v,mid+1,r);
        merge(v,l,r,mid);
    }
}
signed main()
{
    int n; cin>>n;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        cin>>v[i];
    }
    mergeSort(v,0,n-1);
    for(int i=0; i<n; i++){
        cout<<v[i]<<" ";
    }
    return 0;
}