#include<iostream>
using namespace std;

int binarySearch(int arr[], int size, int key) {

    int start = 0;
    int end = size-1;

    int mid = start + (end-start)/2;

    while(start <= end) {

        if(arr[mid] == key) {
            return mid;
        }

       //for right part
        if(key > arr[mid]) {
            start = mid + 1;
        }
        else{ //for left part
            end = mid - 1;
        }

        mid = start + (end-start)/2;
    }
    
    return -1;
}


int main() { 

    int even[100] ,t,val1;
    int odd[100],r,val2;
    cout<<"enter number of elememts in even array"<<endl;
cin>>t;
     cout<<"enter number of elememts in even array"<<endl;
     cin>>r;
     cout<<"enter the element of even array"<<endl;
    for (int i = 0; i < t; ++i) {
    cin >> even[i];
  }
   cout<<"enter the element of odd array"<<endl;
  for (int i = 0; i < r; ++i) {
    cin >> odd[i];
  }
   cout<<"enter value 1"<<endl;
cin>>val1;
 cout<<"enter value 2"<<endl;
cin>>val2;

    int evenIndex = binarySearch(even, t, val1);

    cout << " Index of 6 is " << evenIndex << endl;

    int oddIndex = binarySearch(odd, r, val2);

    cout << " Index of 14 is " << oddIndex << endl;


    return 0;
}

int findPeak(int arr[], int n) {

    int s =0, e = n-1;
    int mid = s + (e-s)/2;

    while(s<e) {
        //cout<<" s " << s <<" e " << e << endl;
        if(arr[mid] < arr[mid+1]){
            s = mid+1; 
        }
        else{
            e = mid;
        }
        mid = s + (e-s)/2;
    }
    return s;
}