from typing import List

# LeetCode 349 - Intersection of Two Arrays
# Difficulty: Easy
# Pattern: Hash Set
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2_set = set(nums2)

        for num in nums1:
            if num in nums2_set:
                result.add(num)

        return list(result)