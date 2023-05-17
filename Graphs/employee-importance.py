# https://leetcode.com/problems/employee-importance/



"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # we are asked to find the total importance of a given id, and its direct subbordinates
        # step 1 : create a mapping from employee id to importance and subbordinates for a given id
        
        importance, subordinates = {}, {}
        for employee in employees:
            importance[employee.id] = employee.importance
            subordinates[employee.id] = employee.subordinates
        
        # then sum importance by DFS (get importance root employee recursively)
        # finally add importance totals of subordinates
        
        def sum_imp(imp_id): # ret(imp_id and plus recursive sum of subordinates)
            total = importance[imp_id]
            for sub in subordinates[imp_id]:
                total += sum_imp(sub)
            return total 
        return sum_imp(id)
    
        # Time Complexity = O(n)
        # Space Complexity = O(n)
