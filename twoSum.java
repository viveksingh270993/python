import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // prevMap stores <Value, Index>
        Map<Integer, Integer> prevMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;
            
            // Check if the complement exists in the map
            if (prevMap.containsKey(diff)) {
                return new int[] { prevMap.get(diff), i };
            }
            
            // If not found, add current number and its index to map
            prevMap.put(num, i);
        }
        
        // Return empty array if no solution is found
        return new int[] {};
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        
        int[] result = sol.twoSum(nums, target);
        
        if (result.length == 2) {
            System.out.println("[" + result[0] + ", " + result[1] + "]");
        }
    }
}
