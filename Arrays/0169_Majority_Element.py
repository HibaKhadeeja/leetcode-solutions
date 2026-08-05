from typing import List

# LeetCode 169 - Majority Element
# Difficulty: Easy
# Pattern: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None

        for num in nums:
            if count == 0:
                element = num

            if num == element:
                count += 1
            else:
                count -= 1

        return element