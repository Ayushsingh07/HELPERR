import java.util.Arrays;

class Main
{
	public static void swap (int[] arr, int i, int j)
	{
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	// Partition using the Lomuto partition scheme
	public static int partition(int[] a, int start, int end)
	{
		// Pick the rightmost element as a pivot from the array
		int pivot = a[end];

		// elements less than the pivot will be pushed to the left of `pIndex`
		// elements more than the pivot will be pushed to the right of `pIndex`
		// equal elements can go either way
		int pIndex = start;

		// each time we find an element less than or equal to the pivot,
		// `pIndex` is incremented, and that element would be placed
		// before the pivot.
		for (int i = start; i < end; i++)
		{
			if (a[i] <= pivot)
			{
				swap(a, i, pIndex);
				pIndex++;
			}
		}

		// swap `pIndex` with pivot
		swap(a, end, pIndex);

		// return `pIndex` (index of the pivot element)
		return pIndex;
	}

	// Quicksort routine
	public static void quicksort(int[] a, int start, int end)
	{
		// base condition
		if (start >= end) {
			return;
		}

		// rearrange elements across pivot
		int pivot = partition(a, start, end);

		// recur on subarray containing elements less than the pivot
		quicksort(a, start, pivot - 1);

		// recur on subarray containing elements more than the pivot
		quicksort(a, pivot + 1, end);
	}

	// Java implementation of the Quicksort algorithm
	public static void main(String[] args)
	{
		int[] a = { 9, -3, 5, 2, 6, 8, -6, 1, 3 };

		quicksort(a, 0, a.length - 1);

		// print the sorted array
		System.out.println(Arrays.toString(a));
	}
}





Output:

[-6, -3, 1, 2, 3, 5, 6, 8, 9]

