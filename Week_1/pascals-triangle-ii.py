# https://leetcode.com/problems/pascals-triangle-ii/description/



class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Base case
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        
        # recursive case
        prev_row = self.getRow(rowIndex - 1)
        curr_row = [1]

        for i in range(len(prev_row)-1):
            curr_row.append(prev_row[i] + prev_row[i+1])
        curr_row.append(1) #append 1 at the end : always after the recursion
        return curr_row
