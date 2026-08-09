from typing import List

# LeetCode 228 - Summary Ranges
# Difficulty: Easy
# Pattern: Array / Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n) for the output

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(str(nums[start]) + "->" + str(nums[i - 1]))

                start = i

        if nums:
            if start == len(nums) - 1:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start]) + "->" + str(nums[-1]))

        return result