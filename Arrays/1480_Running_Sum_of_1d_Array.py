from typing import List

# LeetCode 1480 - Running Sum of 1d Array
# Difficulty: Easy
# Pattern: Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums