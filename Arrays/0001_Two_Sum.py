# LeetCode 1 - Two Sum
# Difficulty: Easy
# Pattern: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i