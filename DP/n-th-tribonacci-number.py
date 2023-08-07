# https://leetcode.com/problems/n-th-tribonacci-number/description/



class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0,1,1]
        while len(nums) <= n:
            nums.append(sum(nums[-3:]))
        return nums[n]
