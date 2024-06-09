class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Wtf time limit exceeded
        # n = len(nums)
        # if n == 1 or n == 0:
        #     return False
        # starting_sum = sum(nums)
        # if starting_sum % k == 0:
        #     return True
        # for start in range(n - 1):
        #     if start != 0:
        #         subarray_sum = starting_sum - nums[start-1]
        #         starting_sum = subarray_sum
        #         if subarray_sum % k == 0:
        #             return True
        #     else:
        #         subarray_sum = starting_sum

        #     for end in range(n-1, start + 1, -1): 
        #         subarray_sum -= nums[end]
        #         if subarray_sum == 0 and k == 0:  
        #             return True
        #         if k != 0 and subarray_sum % k == 0: 
        #             return True
        # return False

        # another tle logic
        # n = len(nums)
        # cumulative_sum = [0] * (n + 1)
        
        # # Step 1: Create Cumulative Sums
        # for i in range(1, n + 1):
        #     cumulative_sum[i] = cumulative_sum[i - 1] + nums[i - 1]
        
        # # Step 2: Iterate Through Starting Points
        # for start in range(n):
        #     # Step 3: Expand the Subarray
        #     for end in range(start + 1, n):
        #         # Step 4: Calculate the Sum
        #         subarray_sum = cumulative_sum[end + 1] - cumulative_sum[start]
        #         if subarray_sum == 0 and k == 0:  # Handling special case where k is 0
        #             return True
        #         if k != 0 and subarray_sum % k == 0:  # Step 5: Check if the Sum is a Multiple of k
        #             return True
        # return False  # Step 6: Return the Result

        # Let's use a bit of math.
        # if we just check remainders of various elements from cumulative sums list and 
        # by chance if any two remainders happens to be same it implies that there is 
        # exactly k or multiple of k difference between these 2 elements. The only condition
        # left is they should be atleast two indices apart. Let's implement it using hashmap

        remainder_map = {0: -1}  
        cumulative_sum = 0
        
        for i, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
        return False