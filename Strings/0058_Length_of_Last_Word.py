# LeetCode 58 - Length of Last Word
# Difficulty: Easy
# Pattern: String / Reverse Traversal
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def lengthOfLastWord(self, s):
        c = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if c > 0:
                    return c
            else:
                c += 1

        return c