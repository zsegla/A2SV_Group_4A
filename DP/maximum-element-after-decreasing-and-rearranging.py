# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/



class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        count = defaultdict(int)
        greaterl = 0
        for num in arr:
            count[num]+=1
            if num>len(arr):
                greaterl+=1
        ans = len(arr)
        i = len(arr)
        while i>1:
            if count[i]:
                greaterl+=(count[i]-1)
            else:
                if greaterl>0:
                    greaterl-=1
                else:
                    ans-=1
            i-=1
        return ans
