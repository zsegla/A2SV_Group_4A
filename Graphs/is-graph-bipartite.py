# https://leetcode.com/problems/is-graph-bipartite/



class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colours = [None]*n
        # initially, set all nodes are not coloured

        for i in range(len(graph)):
            if colours[i] is not None:
                continue
            
            colours[i] = True # <- coloured nodes whose edges have not been checked
            queue = deque([i]) # queue contains nodes whose neighbors still need to be explored

            
            while queue:
                v = queue.popleft()
                for nb in graph[v]: # nb is to mean neighbor 
                    if colours[nb] is None:
                        # set to the opposite color of v
                        colours[nb] = not colours[v] 
                        queue.append(nb)
                    # if it is inconsistent, it cannot be bipartite    
                    elif colours[nb] == colours[v]:
                        return False
        return True
