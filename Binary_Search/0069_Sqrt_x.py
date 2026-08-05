# LeetCode 69 - Sqrt(x)
# Difficulty: Easy
# Pattern: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            mid = (l + r) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                l = mid + 1

            else:
                r = mid - 1

        return r