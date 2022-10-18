#include <algorithm>
#include <iostream>
#include <vector>
#include<string>
using namespace std;

void bucketSort(float arr[], int n)
{
	
	vector<float> t[n];

	for (int i = 0; i < n; i++) {
		int bi = n * arr[i]; 
		t[bi].push_back(arr[i]);
[2022-10-18T16:21:30.037Z] Validating found git in: git
	}

	
	for (int i = 0; i < n; i++)
		sort(t[i].begin(), t[i].end());

	int index = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < t[i].size(); j++)
			arr[index++] = t[i][j];
}


int main()
{
	float arr[]= { 0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434 };
	int n = sizeof(arr) / sizeof(arr[0]);
	bucketSort(arr, n);
	cout << "Sorted array is \n";
	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";
	return 0;
}
