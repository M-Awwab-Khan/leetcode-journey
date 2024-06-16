class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        n = len(nums)
        
        for k in range(n - 1, 1, -1): # fixing the k side (from end to 2nd index coz 0th and 1st will be i and j)
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:  # if ith side and jth side's sum > kth side then all nums bw i and j will also satisfy the triangle inequality
                    count += j - i
                    j -= 1
                else:
                    i += 1
                    
        return count