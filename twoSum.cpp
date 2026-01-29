#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // prevMap stores {Value: Index}
        unordered_map<int, int> prevMap;
        
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            // Check if the complement exists in the map
            // .find() returns .end() if the key is not found
            if (prevMap.find(diff) != prevMap.end()) {
                return {prevMap[diff], i};
            }
            
            // If not found, add current number and index to map
            prevMap[nums[i]] = i;
        }
        
        // Return empty vector if no solution is found
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> result = sol.twoSum(nums, target);
    
    if (!result.empty()) {
        cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    }
    
    return 0;
}
