# https://leetcode.com/problems/loud-and-rich/




class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # create a graph mapping to richer people
        #DFS :  update the results of all richer people

        n = len(quiet)
        richer_t = [set() for _ in range(n)]

        for a, b in richer:
            richer_t[b].add(a)
        
        res = [None] * n

        def update_r(person):
            if res[person] is not None:
                return # already found result
            
            res[person] = person # default value : self

            for rich in richer_t[person]:
                update_r(rich) # update teh results of richer people
                # when quiet is < result of richer
                if quiet[res[rich]] < quiet[res[person]]: 
                    res[person] = res[rich]

        for i in range(n):
            update_r(i)
        return res
