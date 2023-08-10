# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/



class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        subset_count = 0
        n = len(nums)
        
        # Iterate through all possible subsets
        for mask in range(1 << n):
            subset_or = 0
            for i in range(n):
                if mask & (1 << i):
                    subset_or |= nums[i]
            
            if subset_or == max_or:
                subset_count += 1
        
        return subset_count
