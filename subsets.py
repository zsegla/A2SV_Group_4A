# https://leetcode.com/problems/subsets/



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, curr):
            result.append(curr[:])
            for i in range(start, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        result, n = [], len(nums)
        backtrack(0, [])
        return result
        
