# https://leetcode.com/problems/number-complement/



class Solution:
    def findComplement(self, num: int) -> int:
        i = 1

        while i <= num:
            i <<= 1

        return (i - 1) ^ num
