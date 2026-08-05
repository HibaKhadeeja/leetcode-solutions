from typing import List

# LeetCode 136 - Single Number
# Difficulty: Easy
# Pattern: Bit Manipulation (XOR)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num

        return ans