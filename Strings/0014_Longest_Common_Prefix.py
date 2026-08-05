# LeetCode 14 - Longest Common Prefix
# Difficulty: Easy
# Pattern: String / Vertical Scanning
# Time Complexity: O(n * m)
# Space Complexity: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        first = strs[0]

        for i in range(len(first)):
            for word in strs:
                if i >= len(word) or first[i] != word[i]:
                    return ans

            ans = ans + first[i]

        return ans