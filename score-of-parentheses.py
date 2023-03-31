# https://leetcode.com/problems/score-of-parentheses/description/


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # time = O(n)
        # space = O(n)

        stack = []
        res, mul = 0, 0
        for i, p in enumerate(s):
            if p == "(":
                mul += 1
            elif p == ")":
                mul -= 1
                if i > 0 and s[i-1] == "(":
                    res += 2**mul
        return res
