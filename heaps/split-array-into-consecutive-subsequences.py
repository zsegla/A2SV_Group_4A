# https://leetcode.com/problems/split-array-into-consecutive-subsequences/



class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        sequences = defaultdict(int)  # map from num to number of sequences ending with num

        for num in nums:

            if freq[num] == 0:  # num already used to extend other sequences
                continue
            freq[num] -= 1

            if sequences[num - 1] != 0:  # extend an existing sequence
                sequences[num - 1] -= 1
                sequences[num] += 1

            elif freq[num + 1] > 0 and freq[num + 2] > 0:  # create a new sequence
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                sequences[num + 2] += 1

            else:  # cannot use num
                return False

        return True
