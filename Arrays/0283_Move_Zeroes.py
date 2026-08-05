from typing import List

# LeetCode 283 - Move Zeroes
# Difficulty: Easy
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1