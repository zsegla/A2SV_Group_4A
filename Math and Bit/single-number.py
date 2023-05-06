# https://leetcode.com/problems/single-number/



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using XOR operation : 0 ^ n = n
        xor = 0
        for num in nums:
            xor ^= num
        return xor
