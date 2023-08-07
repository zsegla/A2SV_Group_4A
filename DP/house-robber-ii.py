# https://leetcode.com/problems/house-robber-ii/



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)  # 1 house has no neighbours

        loot, prev = 0, 0
        for num in nums[1:]:  # do not rob first house
            loot, prev = max(num + prev, loot), loot

        nums[-1] = 0 # do not rob last house
        loot2, prev = 0, 0
        for num in nums:
            loot2, prev = max(num + prev, loot2), loot2

        return max(loot, loot2)
