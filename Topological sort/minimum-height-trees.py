# https://leetcode.com/problems/minimum-height-trees/




class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # remove all nodes having one relation/neighbour
        if n == 1:
            return [0]
        connect = defaultdict(set) # key = node : value = nb nodes
        for a, b in edges:
            connect[a].add(b)
            connect[b].add(a)

        leaves = set(node for node in connect if len(connect[node]) == 1)

        while len(connect) > 2:
            new = set()
            for leaf in leaves:
                nb = connect[leaf].pop()
                connect[nb].remove(leaf)
                if len(connect[nb]) == 1:
                    new.add(nb)
                del connect[leaf]
            leaves = new

        return list(connect.keys())
