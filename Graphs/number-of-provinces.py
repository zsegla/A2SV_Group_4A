# https://leetcode.com/problems/number-of-provinces/



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    if j not in seen:
                        seen.add(j)
                        dfs(j)
        circles = 0
        seen = set()

        for i in range(len(isConnected)):
            if i not in seen:
                circles += 1
                dfs(i)

        return circles
