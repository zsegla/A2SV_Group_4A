# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/



class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        if n <= 4:
            return 0
        
        return min(nums[n-1] - nums[3], nums[n-2] - nums[2], nums[n-3] - nums[1], nums[n-4] - nums[0])
