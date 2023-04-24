# https://leetcode.com/problems/subsets-ii/



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_count = Counter(nums)
        results = [[]]

        for num in num_count:
            results += [partial+[num]*i for i in range(1,num_count[num]+1) for partial in results]

        return results
