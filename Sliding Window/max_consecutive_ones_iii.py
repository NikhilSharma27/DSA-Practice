# LeetCode Problem: https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1706382953/
# Category: Sliding Window (Level 1)
# Approach: Two Pointer with zero count

def longestOnes(nums, k):
    start = 0
    max_len = 0
    zero_count = 0

    for end in range(len(nums)):
        if nums[end] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[start] == 0:
                zero_count -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len

# Example usage:
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# print(longestOnes(nums, k))  # Output: 6
