# https://leetcode.com/problems/single-number-iii/




class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor = xor ^ num

        bit = 0
        while not (1 << bit) & xor:
            bit += 1

        bit_set_xor, bit_not_set_xor = 0, 0
        for num in nums:
            if (1 << bit) & num:
                bit_set_xor = bit_set_xor ^ num
            else:
                bit_not_set_xor = bit_not_set_xor ^ num

        return [bit_set_xor, bit_not_set_xor]
