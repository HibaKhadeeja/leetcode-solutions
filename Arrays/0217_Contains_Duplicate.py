# LeetCode 217 - Contains Duplicate
# Difficulty: Easy
# Pattern: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        single = set()

        for i in nums:
            if i in single:
                return True

            single.add(i)

        return False