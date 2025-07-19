"""
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/submissions/1702513746/
Approach: Two pointers 
Time: O(n), Space: O(n)
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        clean = ''
        for c in s:
            if c.isalnum():
                clean += c.lower()
        i = 0
        j = len(clean)-1
        while i <= j :
            if clean[i]==clean[j]:
                i+=1
                j-=1
            else:
                return False
        return True

        
