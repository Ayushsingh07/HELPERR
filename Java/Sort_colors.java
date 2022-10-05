// https://leetcode.com/problems/sort-colors/


class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        for(int i =0;i<n;i++){
            for(int j = 0;j<n-1;j++){
                if(nums[j]>nums[j+1]){
                    swap(nums,j,j+1);
                }
            }
        }
    }
    static void swap(int[] nums , int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
