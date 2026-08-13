# LeetCode 1486 - XOR Operation in an Array
# Difficulty: Easy
# Pattern: Bit Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0

        for i in range(n):
            result ^= start + 2 * i

        return result