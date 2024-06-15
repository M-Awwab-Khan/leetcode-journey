class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int n = nums.size();
        int windowSize = 2 * k + 1;
        vector<int> result(n, -1);
        long long total = 0;

        for(int i = 0; i < n; i++){
            total += nums[i];
         
            if(i >= windowSize - 1){
                result[i - windowSize / 2] = total / windowSize;
                total -= nums[i - windowSize + 1];
            }
        }

        return result;
    }
};