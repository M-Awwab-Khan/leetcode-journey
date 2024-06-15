class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int min_length = INT_MAX;
        int sum = 0;
        int i = 0;
        
        for (int j = 0; j < nums.size(); ++j) {
            sum += nums[j];
            while (sum >= target) {
                min_length = min(min_length, j - i + 1);
                sum -= nums[i++];
            }
        }
        
        return min_length != INT_MAX ? min_length : 0;
    }
};