class Solution {
public:
    int commonFactors(int a, int b) {
        int gcd = __gcd(a, b);
        int factors = 0;
        for (int i = 1; i <= sqrt(gcd); ++i) {
            if (gcd % i == 0) {
                factors++;
                if (i != gcd / i) factors++;
            }
        }

        return factors;
    }
};