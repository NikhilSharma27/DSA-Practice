"""
Problem: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/submissions/1694369311/
Approach: Two-pointer style - move non-zeroes forward, fill rest with 0
Time: O(n), Space: O(1)
"""

def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    for k in range(i, len(nums)):
        nums[k] = 0
    return nums

# Example
nums = [0, 1, 0, 3, 12]
print("After MoveZeroes:", moveZeroes(nums))  # [1, 3, 12, 0, 0]
