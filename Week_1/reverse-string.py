# https://leetcode.com/problems/reverse-string/description/



class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Two pointer approach
        # l, r = 0, len(s) - 1
        
        # while s and l <= r:
        #     s[l], s[r] = s[r], s[l]
        #     l += 1
        #     r -= 1

        # recursively
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        reverse(0, len(s)-1)
