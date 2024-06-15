class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        while (l < r) {
            int s = numbers[l] + numbers[r];
            if (s < target) l++;
            else if (s > target) r--;
            else return vector<int> {l+1, r+1};
        }
        return vector<int> {l+1, r+1};
    }
};