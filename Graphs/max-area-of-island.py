# https://leetcode.com/problems/max-area-of-island/


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        def island_area(r, c):

            grid[r][c] = 0
            area = 1

            for dr, dc in neighbours:       # faster to check valid land cell before recursing
                if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 1:
                    area += island_area(r + dr, c + dc)

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:     # check only occupied cells
                    max_area = max(max_area, island_area(row, col))

        return max_area
