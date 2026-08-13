from typing import List

# LeetCode 724 - Find Pivot Index
# Difficulty: Easy
# Pattern: Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1