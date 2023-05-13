# https://leetcode.com/problems/beautiful-arrangement/



class Solution:
    def countArrangement(self, n: int) -> int:
        used = [False for _ in range(n + 1)]
        self.count = 0

        def helper(i):          # i is position to be filled
            if i == 0:          # solution found
                self.count += 1
                return

            for num in range(1, n + 1):
                if not used[num] and (num % i == 0 or i % num == 0):
                    used[num] = True
                    helper(i - 1)
                    used[num] = False

        helper(n)
        return self.count
