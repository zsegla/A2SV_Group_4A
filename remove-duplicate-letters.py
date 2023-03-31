# https://leetcode.com/problems/remove-duplicate-letters/description/



class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s_set = sorted(set(s))
        for c in s_set:
            suffix = s[s.index(c):]
            if len(set(suffix)) == len(s_set):
                return c + self.removeDuplicateLetters(suffix.replace(c, ""))
        return ""
