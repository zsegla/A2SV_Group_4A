# https://leetcode.com/problems/hamming-distance/



class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming = 0

        while x or y:
            hamming += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1

        return hamming
