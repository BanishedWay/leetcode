package day04;

public class MissingNumber {
    public int missingNumber(int[] nums) {
        /*
        尝试用二分查找判断
        当mid==i时，表明缺失的数字在mid右侧，否则在左侧
         */
        int left = 0, right = nums.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] != mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
