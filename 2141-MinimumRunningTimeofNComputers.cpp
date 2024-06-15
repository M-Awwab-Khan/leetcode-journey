class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        auto canRunFor = [&](long long t) -> bool {
            long long total = 0;
            for (const auto& battery : batteries) {
                total += min(static_cast<long long>(battery), t);
            }
            return total >= n * t;
        };

        long long left = 0, right = accumulate(batteries.begin(), batteries.end(), 0LL) / n;
        while (left < right) {
            long long mid = (left + right + 1) / 2;
            if (canRunFor(mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }

        return left;
    }
};