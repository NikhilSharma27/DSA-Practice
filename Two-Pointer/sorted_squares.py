"""
Problem: Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/1694337068/
Approach: Two-pointer from both ends, fill largest square from the back
Time: O(n), Space: O(n)
"""

def sortedSquares(nums):
    i = 0
    j = len(nums) - 1
    pos = len(nums) - 1
    output = [0] * len(nums)

    while i <= j:
        left_val = nums[i] ** 2
        right_val = nums[j] ** 2
        if left_val < right_val:
            output[pos] = right_val
            j -= 1
        else:
            output[pos] = left_val
            i += 1
        pos -= 1

    return output
