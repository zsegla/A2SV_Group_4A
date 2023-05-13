# https://leetcode.com/problems/sum-of-two-integers/



class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF       # 2**32 - 1
        MAX_INT = 0x7FFFFFFF    # 2**31 - 1

        while b != 0:

            total = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK   # shift pattern when both bits are set
            print(a, b, total, carry)
            a, b = total, carry

        return a if a < MAX_INT else ~(a ^ MASK)    # a - 2**321
