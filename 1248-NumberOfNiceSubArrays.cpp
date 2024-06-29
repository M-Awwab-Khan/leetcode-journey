class Solution {
public:
    int atmostK(vector<int>& v, int k)
    {
        int left = 0, right = 0;
        int odds = 0, ans = 0;
        while (right < v.size())
        {
            if (v[right] % 2 == 1) odds++;
            
            while (odds > k) {
                if(v[left++] % 2 == 1) odds--;
            }
            ans += (right - left + 1);
            right++;
        }
        return ans;
    }
    int numberOfSubarrays(vector<int>& nums, int k) {
        return atmostK(nums, k) - atmostK(nums, k-1);
    }
};