# https://leetcode.com/problems/unique-paths/



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        row_paths = [1 for _ in range(n)]       # first row, one path to each column

        for row in range(m-1):
            new_row_paths = [1]                 # one path to first col of each row
            for col in range(1, n):
                new_row_paths.append(new_row_paths[-1] + row_paths[col])
            row_paths = new_row_paths

        return row_paths[-1]
