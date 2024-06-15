class Solution {
public:
    int maxScore(vector<int>& v, int k) {
        int sum=accumulate(v.begin(),v.end(),0);
        int left=0;
        int ans=v[0];
        int s=accumulate(v.begin(), v.end() - k, 0);
        int n = v.size();
        for(int i = 0; i < k; i++){
            ans=max(ans,sum-s);
            s+=v[n-k+i];
            s-=v[i];
            ans=max(ans,sum-s);
        }
        return ans;
    }
};