# LeetCode 125 - Valid Palindrome
# Difficulty: Easy
# Pattern: String Processing
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isPalindrome(self, s):
        new = ""

        for i in s:
            if i.isalnum():
                new += i.lower()

        return new == new[::-1]