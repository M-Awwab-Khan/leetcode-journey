class Solution {
public:
    bool isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }

        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }

        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }

        return true;
    }
    int diagonalPrime(vector<vector<int>>& nums) {
        int dim = nums.size();
        int maxPrime = 0;
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                if (i == j || i == dim - j - 1) {
                    if (isPrime(nums[i][j])) {
                        maxPrime = max(maxPrime, nums[i][j]);
                    }
                }
            }
        }
        return maxPrime;
    }
};