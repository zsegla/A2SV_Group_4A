# https://leetcode.com/problems/n-queens/



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        partials = [[]]                         # solutions up to current row
        for col in range(n):
            new_partials = []
            for partial in partials:
                for row in range(n):
                    if not self.conflict(partial, row):
                        new_partials.append(partial + [row])
            partials = new_partials

        results = []
        for partial in partials:                # convert result to strings
            result = [['.'] * n for _ in range(n)]
            for col, row in enumerate(partial):
                result[row][col] = 'Q'
            for row in range(n):
                result[row] = ''.join(result[row])
            results.append(result)

        return results

    def conflict(self, partial, new_row):
        for col, row in enumerate(partial):
            if new_row == row:                      # same row
                return True
            col_diff = len(partial) - col
            if abs(new_row - row) == col_diff:      # same diagonal
                return True

        return False
