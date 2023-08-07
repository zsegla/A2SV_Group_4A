# https://leetcode.com/problems/previous-permutation-with-one-swap/description/



class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 2, -1, -1):

            if arr[i] > arr[i + 1]:# A can be made smaller by swapping a smaller digit to A[i]
                max_seen = -1
                for j in range(len(arr) - 1, i, -1):
                    if arr[j] >= max_seen and arr[j] < arr[i]:
                        max_seen = arr[j]
                        max_seen_index = j

                arr[i], arr[max_seen_index] = arr[max_seen_index], arr[i]   
                break

        return arr
        # time = O(n)
        # space = O(1)
