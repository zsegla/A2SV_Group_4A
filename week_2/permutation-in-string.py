# https://leetcode.com/problems/permutation-in-string/description/



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N = len(s1)
        freq = [0]*26

        for c in s1:
            freq[ord(c) - ord("a")] += 1

        for i, c in enumerate(s2):
            freq[ord(c)-ord("a")] -= 1
            if i >= N:
                freq[ord(s2[i-N]) - ord("a")] += 1  
            if not any(freq):
                return True 
        return False 
