class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> numbersHashSet = new HashSet<>();
        for (int i =0; i<nums.length; i++) {
            if (numbersHashSet.contains(nums[i])) return true;
            numbersHashSet.add(nums[i]);
        }
        return false;
    }
}