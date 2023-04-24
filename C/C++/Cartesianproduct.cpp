// C++ Program to find the Cartesian Product of Two Sets
#include <stdio.h>

void findCart(int arr1[], int arr2[], int n, int n1)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n1; j++)
			printf("{%d, %d}, ", arr1[i], arr2[j]);
}

int main()
{
	int arr1[] = { 1, 2, 3 }; // first set
	int arr2[] = { 4, 5, 6 }; // second set
	int n1 = sizeof(arr1) / sizeof(arr1[0]);
	int n2 = sizeof(arr2) / sizeof(arr2[0]);
	findCart(arr1, arr2, n1, n2);
	return 0;
}
