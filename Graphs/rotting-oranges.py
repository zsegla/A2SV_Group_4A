# https://leetcode.com/problems/rotting-oranges/



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, rotten = set(), set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                if grid[r][c] == 2:
                    rotten.add((r, c))

        mins = 0
        while fresh:
            mins += 1
            new_rotten = set()

            for r, c in rotten:
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:   # check all neighbours
                    if (r + dr, c + dc) in fresh:
                        new_rotten.add((r + dr, c + dc))

            if not new_rotten:
                return -1
            rotten = new_rotten
            fresh -= new_rotten

        return mins
