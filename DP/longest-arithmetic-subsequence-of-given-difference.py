# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/



class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {} 
        for num in arr:
            prev_num = num - difference
            dp[num] = dp.get(prev_num, 0) + 1

        return max(dp.values())
