"""
Problem: Reverse String
Link: https://leetcode.com/problems/reverse-string/submissions/1694292809/
Approach: Two-pointer from both ends swapping characters in-place
Time: O(n), Space: O(1)
"""

def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# Example
input_str = ["h","e","l","l","o"]
print("Reversed:", reverseString(input_str))  # ['o', 'l', 'l', 'e', 'h']
