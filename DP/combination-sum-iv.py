# https://leetcode.com/problems/combination-sum-iv/description/



class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for ans in range(1, target + 1):
            for num in nums:
                if ans - num >= 0:
                    dp[ans] += dp[ans - num]
        return dp[target]
