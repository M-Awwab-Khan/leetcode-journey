class Solution {
public:
    void primeFactors(int c, unordered_map<int,int> &freq){
        // finding the prime factors
        for(int n=2; n<sqrt(c)+1; n++){
            while(c%n == 0){
                c/=n;
                freq[n]++;
            }
        }
        // last prime factor
        if(c>2) freq[c]++;
    }

    bool judgeSquareSum(int c) {
        // Using Fermat's theorem: if c has a prime factor of the type 4k+3 and of odd power, then c cant be expressed as a sum of 2 squares

        if(c==0) return true;

        unordered_map<int,int> prime_factors;
        primeFactors(c, prime_factors);

        // checking for fermat's theorem validity
        for(auto it= prime_factors.begin() ; it!=prime_factors.end(); ++it){
            if( ((it->first - 3) % 4 == 0) && it->second % 2 != 0) return false;
        }
        return true;
    }
};