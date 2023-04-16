package day04;

public class Search {
    public int search(int[] nums, int target) {
        //使用二分查找找到第一个与target相等的元素
        int left = 0, right = nums.length, count = 0;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        while (left < nums.length && nums[left] == target) {
            left++;
            count++;
        }
        return count;
    }
}
