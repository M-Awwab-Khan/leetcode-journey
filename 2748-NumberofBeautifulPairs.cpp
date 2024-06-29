class Solution {
public:
    int firstDigit(int n) 
    { 
        while (n >= 10)  
            n /= 10; 
        
        return n; 
    } 
    
    int lastDigit(int n) 
    { 
        return (n % 10); 
    } 
    int countBeautifulPairs(vector<int>& nums) {
        int pairs = 0;
        int n = nums.size();
       for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (__gcd(firstDigit(nums[i]), lastDigit(nums[j])) == 1)  pairs++;
        }
       }

        return pairs;
    }
};