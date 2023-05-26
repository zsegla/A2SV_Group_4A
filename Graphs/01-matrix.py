# https://leetcode.com/problems/01-matrix/



class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        queue = deque()
        result = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    result[i][j] = 0

        while queue:
            x, y = queue.popleft()
            for dx, dy in direct:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and result[nx][ny] > result[x][y] + 1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))

        return result
