package day04;

public class FindRepeatNumber {
    public int findRepeatNumber(int[] nums) {
//        Set<Integer> set = new HashSet<Integer>();
//        for (int num : nums) {
//            //当num不能被加入时，表明此时set中存在相同元素
//            if (!set.add(num)) {
//                return num;
//            }
//        }
        for (int i = 0; i < nums.length; i++) {
            int k = nums[i];
            if (k < 0) k += nums.length;
            if (nums[k] < 0) return k;//当nums[k]小于0时，表明前面已经存入k
            else nums[k] -= nums.length;//当k第一次出现时，将nums[k]小于0
        }
        return -1;
    }
}
