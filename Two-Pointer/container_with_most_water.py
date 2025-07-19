"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/submissions/1703312439/
Approach: Two Pointers – Move the shorter line inward to try for a taller one.
Time: O(n), Space: O(1)
"""

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        area = h * w
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
