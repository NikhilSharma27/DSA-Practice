"""
Problem: Minimum Size Subarray Sum
Link: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1703527158/
"""

def minSubArrayLen(target, nums):
    start = 0 
    window_sum = 0
    min_len = float('inf')

    for end in range(len(nums)):
        window_sum += nums[end]

        while window_sum >= target:
            min_len = min(min_len, end - start + 1)
            window_sum -= nums[start]
            start += 1

    return 0 if min_len == float('inf') else min_len

# Example
# target = 7, nums = [2,3,1,2,4,3]
# Output: 2
