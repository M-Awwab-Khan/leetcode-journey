#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> minDeque, maxDeque;
        int left = 0, right = 0, maxLength = 0;

        while (right < nums.size()) {
            // Maintain the minDeque to store the index of minimum elements in the current window
            while (!minDeque.empty() && nums[minDeque.back()] >= nums[right]) {
                minDeque.pop_back();
            }
            minDeque.push_back(right);

            // Maintain the maxDeque to store the index of maximum elements in the current window
            while (!maxDeque.empty() && nums[maxDeque.back()] <= nums[right]) {
                maxDeque.pop_back();
            }
            maxDeque.push_back(right);

            // Check if the current window is valid
            while (nums[maxDeque.front()] - nums[minDeque.front()] > limit) {
                left++;
                if (minDeque.front() < left) {
                    minDeque.pop_front();
                }
                if (maxDeque.front() < left) {
                    maxDeque.pop_front();
                }
            }

            // Calculate the length of the current valid window
            maxLength = max(maxLength, right - left + 1);
            right++;
        }

        return maxLength;
    }
};