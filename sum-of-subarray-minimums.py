# https://leetcode.com/problems/sum-of-subarray-minimums/description/



class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [float("-inf")] + arr + [float("-inf")]
        res = 0 
        stack = []

        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                j = stack.pop()
                res += arr[j] * (j - stack[-1]) * (i - j)
            stack.append(i)
        return res % (10**9+7)
