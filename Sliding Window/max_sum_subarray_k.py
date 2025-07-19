"""
Problem: Maximum Sum Subarray of Size K
Link: https://leetcode.com/problems/maximum-average-subarray-i/submissions/1703440321/
"""

def maxSumSubarrayK(nums, k):
    current_sum = 0
    max_sum = float('-inf')

    for i in range(k):
        current_sum += nums[i]
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum = current_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example
# nums = [2,1,5,1,3,2], k = 3
# Output: 9
