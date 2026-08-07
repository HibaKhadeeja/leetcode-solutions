# LeetCode 383 - Ransom Note
# Difficulty: Easy
# Pattern: Hash Map (Dictionary)
# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}

        for ch in magazine:
            if ch not in seen:
                seen[ch] = 1
            else:
                seen[ch] += 1

        for ch in ransomNote:
            if ch in seen and seen[ch] >= 1:
                seen[ch] -= 1
            else:
                return False

        return True