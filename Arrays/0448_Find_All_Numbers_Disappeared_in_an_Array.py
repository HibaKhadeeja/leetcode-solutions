from typing import List

# LeetCode 448 - Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Pattern: Array / In-place Index Marking
# Time Complexity: O(n)
# Space Complexity: O(1) extra space

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res