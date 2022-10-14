#include<iostream>
using namespace std;

void reverse(int arr[], int n) {

    int start = 0;
    int end = n-1;

    while(start<=end) {
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
}

void printArray(int arr[], int n) {
    
    for(int i=0; i<n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {

    int arr[100] ,t;
    cout<<"enter the number of elements here"<<endl;
cin>>t;
  for (int i = 0; i < t; ++i) {
    cin >> arr[i];
  }
    reverse(arr, t);
   
    printArray(arr, t);
   

    return 0;
}