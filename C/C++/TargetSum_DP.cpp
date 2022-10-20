#include <bits/stdc++.h>
using namespace std;
int mod =(int)1e9+7;
int findWays(vector<int> &num, int tar){
     int n = num.size();

    vector<int> prev(tar+1,0);
    
    if(num[0] == 0) prev[0] =2;  // 2 cases -pick and not pick
    else prev[0] = 1;  // 1 case - not pick
    
    if(num[0]!=0 && num[0]<=tar) prev[num[0]] = 1;  // 1 case -pick
    
    for(int ind = 1; ind<n; ind++){
        vector<int> cur(tar+1,0);
        for(int target= 0; target<=tar; target++){
            int notTaken = prev[target];
    
            int taken = 0;
                if(num[ind]<=target)
                    taken = prev[target-num[ind]];
        
            cur[target]= (notTaken + taken)%mod;
        }
        prev = cur;
    }
    return prev[tar];
}

int targetSum(int n, int target, vector<int>& arr){
    int totSum = 0;
    for(int i=0; i<n;i++){
        totSum += arr[i];
    }
    if(totSum-target <0 || (totSum-target)%2 ) return 0;
    
    return findWays(arr,(totSum-target)/2);
}
int main() {

  vector<int> arr = {1,2,3,1};
  int n = arr.size();
  int target=3;
                                 
  cout<<"The number of subsets found is " <<targetSum(n,target,arr);
}