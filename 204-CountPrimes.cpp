class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2) {
            return 0;
        }
        
        std::vector<bool> is_prime(n, true);
        is_prime[0] = is_prime[1] = false;
        
        for (int i = 2; i * i < n; ++i) {
            if (is_prime[i]) {
                for (int j = i * i; j < n; j += i) {
                    is_prime[j] = false;
                }
            }
        }
        
        return std::count(is_prime.begin(), is_prime.end(), true);
    }
};