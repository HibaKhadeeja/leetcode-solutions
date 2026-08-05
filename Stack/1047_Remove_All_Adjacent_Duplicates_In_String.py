# LeetCode 1047 - Remove All Adjacent Duplicates In String
# Difficulty: Easy
# Pattern: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def removeDuplicates(self, s):
        stack = []

        for i in s:
            if len(stack) == 0:
                stack.append(i)

            elif stack[-1] == i:
                stack.pop()

            else:
                stack.append(i)

        return "".join(stack)