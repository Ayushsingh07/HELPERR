/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 //  https://leetcode.com/problems/find-in-mountain-array/
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
      int start =0;
        int end = mountainArr.length()-1;
        int mid = start + (end-start)/2;
        while(start<end){
            mid = start + (end-start)/2;
            if(mountainArr.get(mid)<mountainArr.get(mid+1)){
                start = mid +1;
            }
            else{
                end = mid;
            }
        }
        int peak = start;
        start = 0;
        end = peak;
        mid = start + (end-start)/2;
        while(start<=end){
            mid = start + (end-start)/2;
            if(mountainArr.get(mid)>target){
                end = mid -1;;
            }
            else if(mountainArr.get(mid)<target){
                start = mid +1;
            }
                else return mid;
        }
         start = peak +1;
         end = mountainArr.length()-1;
         mid = start + (end-start)/2;
        while(start<=end){
            mid = start + (end-start)/2;
            if(mountainArr.get(mid)>target){
                start = mid +1;
            }
            else if(mountainArr.get(mid)<target){
                end = mid - 1;
            }
                else return mid;  
    }
        return -1;
    }
}
