# https://leetcode.com/problems/course-schedule/



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        order = []
        n_prereq = defaultdict(int)   # key = course ; value = no. of prereq couses
        prereq = defaultdict(list)    # key = course ; value = courses depend on the course


        for after, before in prerequisites:
            n_prereq[after] += 1 
            prereq[before].append (after)
        
        take = set(i for i in range(numCourses)) - set(n_prereq.keys()) # the courses I can take

        while take:
            c = take.pop() # take any course with no prerequisites
            #decrement count of remaining courses to be taken
            numCourses -= 1
            
            for dep in prereq[c]: # dep = dependent 
                n_prereq[dep] -= 1 # decrease the count of dependencies
                if n_prereq[dep] == 0: # no more prerequisite
                    take.add(dep)
        return numCourses == 0
