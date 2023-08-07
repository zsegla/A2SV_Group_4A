# https://leetcode.com/problems/minimize-maximum-of-array/



class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            prefix_avg = -(-prefix // (i + 1)) 
            ans = max(ans, prefix_avg)

        return ans
