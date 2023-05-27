# https://leetcode.com/problems/all-paths-from-source-to-target/



class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, results = [[0]], []      

        while paths:
            new_paths = []

            for path in paths:
                for next_node in graph[path[-1]]:
                    destination = results if next_node == len(graph) - 1 else new_paths
                    destination.append(path[:] + [next_node])

            paths = new_paths

        return results
