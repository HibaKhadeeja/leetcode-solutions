# LeetCode 20 - Valid Parentheses
# Difficulty: Easy
# Pattern: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isValid(self, s):
        stack = []

        d = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            elif ch in ")]}":
                if len(stack) == 0:
                    return False

                elif stack[-1] == d[ch]:
                    stack.pop()

                else:
                    return False

        return len(stack) == 0