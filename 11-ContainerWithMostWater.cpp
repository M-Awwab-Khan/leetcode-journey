class Solution {
public:
    int maxArea(vector<int>& height) {
        int r = height.size() - 1, l = 0, mx = 0;
        while (l < r) {
            mx = max(mx, min(height[r], height[l]) * (r- l));
            if (height[l] < height[r]) l++;
            else r--;
        }
        return mx;
    }
};