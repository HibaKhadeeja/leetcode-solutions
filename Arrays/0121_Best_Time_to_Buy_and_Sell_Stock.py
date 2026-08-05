from typing import List

# LeetCode 121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Pattern: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0

        for p in prices:
            if p < minp:
                minp = p

            pro = p - minp

            if pro > maxp:
                maxp = pro

        return maxp