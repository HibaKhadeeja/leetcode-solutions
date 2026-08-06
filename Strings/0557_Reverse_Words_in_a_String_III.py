from typing import List

# LeetCode 557 - Reverse Words in a String III
# Difficulty: Easy
# Pattern: Strings
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        words = s.split()

        for word in words:
            res.append(word[::-1])

        return " ".join(res)