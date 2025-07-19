"""
Problem: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1702551796/
Approach: Two Pointers – In-place overwrite duplicates with unique elements.
Time: O(n), Space: O(1)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1
